import os
import threading
import pickle

from sqlalchemy import and_

from manager import *
from _server import TypeServer
from project_settings import ROOT_DIR


class ClientThread(threading.Thread):

    def __init__(self, _socket, _address, type_server):
        threading.Thread.__init__(self)
        self.__socket = _socket
        self.__address = _address
        self.type_server_authentication = type_server

        self.connect_data = engine1.connect()

        print("Подключился", _address)

    def run(self):
        msg = ""
        while True:

            try:
                read_access = True
                write_access = True
                delete_access = True

                data = self.receive_data(self.__socket, 4096)
                msg = data.decode()
                if msg == "":
                    self.close_connection()
                    return

                parameters = msg.split()

                block = False
                user = parameters[0]
                table = parameters[1]
                request = parameters[2]

                # authorization
                if self.type_server_authentication == TypeServer.MAC:

                    m = mac.select().where(mac.columns.user_name == user)
                    object_m = object_mac.select().where(object_mac.columns.table_name == table)

                    res1 = self.connect_data.execute(m).fetchone()
                    res2 = self.connect_data.execute(object_m).fetchone()

                    if res1 is None or res2 is None:
                        raise Exception("not found")

                    user_access_level = res1[1]
                    table_access_level = res2[1]

                    if user_access_level == "high" and table_access_level == "low":
                        write_access = False
                        delete_access = False
                    if user_access_level == "low" and table_access_level == "high":
                        read_access = False
                        delete_access = False


                elif self.type_server_authentication == TypeServer.DAC:

                    d = dac.select().where(and_(dac.columns.user_name == user, dac.columns.table_name == table))

                    res = self.connect_data.execute(d).fetchone()

                    if res is None:
                        raise Exception('not found')

                    read_access, write_access, delete_access = res[2:]

                elif self.type_server_authentication == TypeServer.RBAC:

                    select_rbac_user = rbac.select().where(rbac.columns.user_name == user)
                    role_data = self.connect_data.execute(select_rbac_user).fetchone()

                    if role_data is None:
                        raise Exception('not found')
                    role = role_data[1]

                    select_user_role_rwd = roles.select().where(roles.columns.role == role)
                    role_rwd = self.connect_data.execute(select_user_role_rwd).fetchone()

                    if role_rwd is None:
                        raise Exception('not found')

                    read_access, write_access, delete_access = role_rwd[1:]

                    select_role_table = roles_tables.select().where(and_(roles_tables.columns.role == role,
                                                                         roles_tables.columns.table_name == table))

                    role_table = self.connect_data.execute(select_role_table).fetchone()

                    if role_table is None:
                        raise Exception('not found')


                result = "Не разрешён доступ!"
                if request == "select" and read_access:

                    if table == "table1":
                        result = self.connect_data.execute(table1.select()).fetchall()

                    if table == "table2":
                        result = self.connect_data.execute(table2.select()).fetchall()

                if request == "insert" and write_access:

                    if table == "table1":
                        self.connect_data.execute(table1.insert().values(
                    {"Column1": int(parameters[3:][0]), "Column2": parameters[3:][1], "Column3": parameters[3:][2],
                     "Column4": int(parameters[3:][3])}
                            ))

                    if table == "table2":
                        self.connect_data.execute(table2.insert().values(parameters[3:]))

                    result = "insert. ok."

                if request == "delete" and delete_access:

                    if table == "table1":
                        self.connect_data.execute(table1.delete().where(table1.columns.id == int(parameters[3])))

                    if table == "table2":
                        self.connect_data.execute(table1.delete().where(table2.columns.NumberOfTelephone == parameters[3]))

                    result = "delete. ok."

                with open(os.path.join(ROOT_DIR, 'audit.txt'), "a") as audit:
                    audit.write(repr(msg))
                    audit.write(". ")
                    audit.write(result if result == "Не разрешён доступ!" else "Разрешён доступ!")
                    audit.write("\n")

                obj_bytes = pickle.dumps(result)

                self.__socket.send(obj_bytes)
                print("send data")
                print()

            except ConnectionAbortedError:
                print("Отсоединился", self.__address)
                self.close_connection()
                print()
                return

            except:
                ob = pickle.dumps("Не разрешён доступ!")
                self.__socket.send(ob)
                self.close_connection()
                with open(os.path.join(ROOT_DIR, 'audit.txt'), "a") as audit:
                    audit.write(repr(msg))
                    audit.write(". ")
                    audit.write("Не разрешён доступ!\n")
                print("send ----")
                return



    def close_connection(self):
        self.connect_data.close()

    def receive_data(self, source, buffer_size):
        request = None
        try:
            request = source.recv(buffer_size)
        except:
            ...
        return request

    def send(self, source, bytes_data):

        try:
            source.send(bytes_data)
        except:
            ...
