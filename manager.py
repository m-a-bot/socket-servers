from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Boolean, PrimaryKeyConstraint


metadata1 = MetaData()

engine1 = create_engine(r"mysql+mysqlconnector://root:z9Cx@localhost:3306/data")

table1 = Table('table1', metadata1,
            Column('id', Integer(), primary_key=True, autoincrement=True),
            Column('Column1', Integer(), nullable=False),
            Column('Column2', String(200), nullable=False),
            Column('Column3', String(200), nullable=False),
            Column('Column4', Integer(), nullable=False)
)

table2 = Table('table2', metadata1,
            Column('NumberOfTelephone', String(150), primary_key=True),
            Column('Column2', String(200), nullable=False),
            Column('Column3', String(200), nullable=False),
            Column('Column4', Integer(), nullable=False)
)

dac = Table('dac', metadata1,
    Column('user_name', String(200), nullable=False),
    Column('table_name', String(200), nullable=False),
    Column('read', Boolean(), nullable=False),
    Column('write', Boolean(), nullable=False),
    Column('delete', Boolean(), nullable=False),
    PrimaryKeyConstraint('user_name', 'table_name', name='uniq_1')
)

mac = Table('mac', metadata1,
    Column('user_name', String(150), primary_key=True),
    Column('access level', String(150))
)

object_mac = Table('object_mac', metadata1,
    Column('table_name', String(150), primary_key=True),
    Column('access level', String(150))
)

rbac = Table('rbac', metadata1,
    Column('user_name', String(150), primary_key=True),
    Column('role', String(150), nullable=False)
)

roles = Table('roles', metadata1,
    Column('role', String(150), primary_key=True),
    Column('read', Boolean(), nullable=False),
    Column('write', Boolean(), nullable=False),
    Column('delete', Boolean(), nullable=False),
)

roles_tables = Table('roles_tables', metadata1,
    Column('role', String(150), nullable=False),
    Column('table_name', String(150), nullable=False),
    PrimaryKeyConstraint('role', 'table_name')
)



def create_tables(metadata, engine):
    metadata.create_all(engine)


if __name__ == "__main__":
    # create_tables(metadata, engine)
    connect = engine1.connect()

    a = table1.insert().values({"Column1":2, "Column2": "Admin", "Column3" : "chief", "Column4": 3})
    b = table1.insert().values({"Column1":4, "Column2": "Tmin", "Column3" : "admin", "Column4": 3})
    c = table2.insert().values(("123456789", "Peter", "user", 5))
    d = table2.insert().values(("223456789","Anatoliy", "student", 5))
    e = table2.insert().values(("323456789","Vova", "pledge", 5))

    connect.execute(a)
    connect.execute(b)
    connect.execute(c)
    connect.execute(d)
    connect.execute(e)

    connect.commit()
    connect.close()
    #
    # connect.execute(a)
    # connect.execute(b)
    # connect.execute(c)
    # connect.execute(d)
    # connect.execute(e)
    #
    # connect.commit()

    # create_tables(metadata1, engine1)
