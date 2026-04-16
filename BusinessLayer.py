import pyodbc as pyo

class BusinessLayer:

    def __init__(self):
        self.server = None
        self.database = None
        self.username = None
        self.password = None

    def validateLogin(self, usernameEnt, passwordEnt, serverEnt, databaseEnt):

        print("Login validation initiated")
        print(f"Server: {serverEnt.get()}")
        print(f"Database: {databaseEnt.get()}")
        print(f"Username: {usernameEnt.get()}")
        print(f"Password: {passwordEnt.get()}")

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

            self.username = usernameEnt.get()
            self.password = passwordEnt.get()
            self.server = serverEnt.get()
            self.database = databaseEnt.get()

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
    def numberOfRowsA(self):

        print("Function A initiated with:")
        print(f"Server: {self.server}")
        print(f"Database: {self.database}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"        
                )
            
            cursor = connection.cursor()
            data = cursor.execute("select count(*) from IN450.dbo.IN450A")
            dataOutput = data.fetchone()[0]
            connection.close()

            return dataOutput

        except Exception as e:
            print(f"Database Error: {e}")
            message = f"Database Error: {str(e)}"
            try:
                connection.close()
            except:
                pass
            return message
                
    # function to display list of names on table B
    def listNamesB(self):

        print("Function B initiated with:")
        print(f"Server: {self.server}")
        print(f"Database: {self.database}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"        
                )
    
            cursor = connection.cursor()
            data = cursor.execute("select first_name+' '+last_name from IN450.dbo.IN450B")
            fetchedData = data.fetchall()
            connection.close()

            nameList = []
            successStatus = True

            for name in fetchedData:
                nameList.append(name[0])

            return nameList, successStatus

        except Exception as e:
            print(f"Database Error: {e}")
            message = f"Database Error: {str(e)}"
            successStatus = False

            try:
                connection.close()
            except:
                pass
            return message, successStatus
    

        # function to display number of rows on table C
    def numberOfRowsC(self):

        print("Function C initiated with:")
        print(f"Server: {self.server}")
        print(f"Database: {self.database}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"        
                )
            
            cursor = connection.cursor()
            data = cursor.execute("select count(*) from IN450.dbo.IN450C")
            dataOutput = data.fetchone()[0]
            connection.close()

            return dataOutput

        except Exception as e:
            print(f"Database Error: {e}")
            message = f"Database Error: {str(e)}"
            try:
                connection.close()
            except:
                pass
            return message

# Used to test funcionality
# bl = BusinessLayer()
# print(bl.numberOfRowsA())

# bl2 = BusinessLayer()
# print(bl2.listNamesB())

