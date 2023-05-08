from XML_Parser import ParseXML
import json
import sqlite3


class Database:
    def __init__(self, db_name, table_name):
        self.dataBase_name = db_name
        self.table_name = table_name
        self.data = ParseXML("UNData.xml")

    def get_parsed_data(self):
        data = self.data.parseXML()
        return data

    def connect(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print("Database created and successfully connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print(f'Error while connecting to sqlite {error}')

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def createTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)

            sqlite_create_table_query = f'''CREATE TABLE IF NOT EXISTS {self.table_name}(
                                            country TEXT, year INTEGER,
                                            value REAL)'''

            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print('SQLite table created')
            cursor.close()

        except sqlite3.Error as error:
            print('Error while creating as a sqlite table', error)

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print('sqlite connection is closed.')

    def insert(self):
        global sqliteConnection
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')

            data = self.get_parsed_data()
            for i in data:
                country = i[0]
                year = i[1]
                value = i[2]
                sqlite_insert_query = f'''INSERT INTO {self.table_name}
                (country, year, value) VALUES(?, ?, ?)'''

                data_tuple = (country, year, value)
                cursor.execute(sqlite_insert_query, data_tuple)
                sqliteConnection.commit()
            print('File inserted successfully as into a table')
            cursor.close()

        except sqlite3.Error as error:
            print(f'Failed to insert data into sqlite table {error}')

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print(f'The sqlite connection is closed')

    def readTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print('connected to SQLite')
            sqlite_select_query = f"SELECT * from {self.table_name}"
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print(f'Total rows are: {len(records)}')
            cursor.close()

        except sqlite3.Error() as error:
            print(f'Failed to read data from sqlite table {error}')

        finally:
            sqliteConnection.close()
            print('The SQLite connection is closed')

    def get_countries(self):
        con = sqlite3.connect(self.dataBase_name)
        cursorObj = con.cursor()
        sel: str = f"SELECT * from {self.table_name}"
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()
        countries = []
        for row in rows:
            if row[0] not in countries:
                countries.append(row[0])

        return countries

    def fetch(self, country):
        con = sqlite3.connect(self.dataBase_name)
        cursorObj = con.cursor()

        sel: str = f"SELECT * from {self.table_name} WHERE country = ?"
        cursorObj.execute(sel,(country,))
        rows = cursorObj.fetchall()

        dict_data = {}
        for row in rows:
            if row[0] == country:
                dict_data[row[1]] = row[2]
        json_string = json.dumps(dict_data)

        return json_string


#s = Database('SQLite_Python.db', 'Database')
# print(s.get_parsed_data())
# s.connect()
# s.createTable()
# s.insert()
# s.readTable()
#print(s.fetch("Turkey"))
#print(s.get_countries())
