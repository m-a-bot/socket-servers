using System;
using System.Collections.Generic;
using Microsoft.Data.Sqlite;

namespace socket_server
{
    internal class DataBaseManager
    {
        private SqliteConnection connection;

        public DataBaseManager() 
        {
            string connectionString = "";

            connection = new SqliteConnection(connectionString);
        }

        public void OpenConnection()
        {
            connection.Open();
        }
    }
}
