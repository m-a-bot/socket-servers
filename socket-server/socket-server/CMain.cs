using Microsoft.Data.Sqlite;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace socket_server
{
    internal class CMain
    {
        public static void Main(string[] args)
        {
            string connectionString = "Data Source=data.db";

            using (var connection = new SqliteConnection(connectionString)) 
            {
                connection.Open();

                string sqlExpression = @"
                    CREATE TABLE IF NOT EXISTS table1(
                        Id INTEGER,
                        Column1,
                        Column2,
                        Column3,
                        PRIMARY KEY (Id)
                    );
                ";

                string sqlExpression1 = @"
                    CREATE TABLE IF NOT EXISTS table2(
                        Number Text,
                        Column1,
                        Column2,
                        PRIMARY KEY (Number)
                    );
                ";

                var com1 = new SqliteCommand(sqlExpression, connection);
                com1.ExecuteNonQuery();

                var com2 = new SqliteCommand(sqlExpression1, connection);
                com2.ExecuteNonQuery();

                //var sqlExp = "INSERT INTO table1(Column1, Column2, Column3) VALUES (@value1, @value2, @value3)";

                //SqliteCommand command = new SqliteCommand(sqlExp, connection);

                //SqliteParameter parameter1 = new SqliteParameter("@value1", "123");
                //SqliteParameter parameter2 = new SqliteParameter("@value2", 123);
                //SqliteParameter parameter3 = new SqliteParameter("@value3", DateTime.Now);

                //command.Parameters.Add(parameter1);
                //command.Parameters.Add(parameter2);
                //command.Parameters.Add(parameter3);

                //command.ExecuteNonQuery();

                SqliteCommand sqliteCommand = new SqliteCommand(@"SELECT * FROM table1;", connection);

                using (var reader = sqliteCommand.ExecuteReader())
                {
                    while (reader.Read()) 
                    {
                        for (int i=0; i<reader.FieldCount; i++) 
                        {
                            Console.Write(Convert.ToByte(reader.GetValue(i)) + " ");
                        }
                        Console.WriteLine();
                    }
                }
                Console.ReadKey();
            }
        }
    }
}
