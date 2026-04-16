import pyodbc as pyo

username = None
password = None
server = None
database = None


class BusinessLayer:

    def __init__(self):
        pass

    def validateLogin(self, usernameEnt, passwordEnt, serverEnt, databaseEnt):

        print("Login validation initiated")

        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={serverEnt.get()};"
                f"DATABASE={databaseEnt.get()};"
                f"UID={usernameEnt.get()};"
                f"PWD={passwordEnt.get()};"        
                )
            
            print("Connection parameters accepted")
            
            cursor = connection.cursor()
            print("Connection established")

            connection.close()
            print("Connection closed")

            username = usernameEnt
            password = passwordEnt
            server = serverEnt
            database = databaseEnt
            print("Session initiated with credentials")

            message = "Connection successful"

            return message

        except Exception as e:
            print("Connection failed")
            message = f"Connection failed: {e}"
            try:
                connection.close()
            except:
                pass
            return message

    # function to display number of rows on table A
    def numberOfRowsA(self, username=username, password=password, server=server, database=database):
        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"UID={username};"
                f"PWD={password};"        
                )
            
            cursor = connection.cursor()
            data = cursor.execute("select count(*) from IN450.dbo.IN450A")
            dataOutput = data.fetchone()[0]
            connection.close()

            return dataOutput

        except Exception as e:
            try:
                connection.close()
            except:
                pass
            print(e)
                
    # function to display list of names on table B
    def listNamesB(self, username=username, password=password, server=server, database=database):
        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"UID={username};"
                f"PWD={password};"        
                )
    
            cursor = connection.cursor()
            data = cursor.execute("select first_name+' '+last_name from IN450.dbo.IN450B")
            fetchedData = data.fetchall()
            connection.close()

            nameList = []

            for name in fetchedData:
                nameList.append(name[0])

            return nameList

        except Exception as e:
            try:
                connection.close()
            except:
                pass
            print(e)
    

# Used to test funcionality
# bl = BusinessLayer()
# print(bl.numberOfRowsA())

# bl2 = BusinessLayer()
# print(bl2.listNamesB())

