import pyodbc as pyo


class BusinessLayer:

    def __init__(self):
        pass

    # function to display number of rows on table A
    def numberOfRowsA(self):
        try:
            connection = pyo.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                r"SERVER=LAPTOP-IUDORUJJ\SQLEXPRESS;"
                r"DATABASE=IN450;"
                r"Trusted_Connection=yes;"        
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
    def listNamesB(self):
        try:
            connection = pyo.connect(
            r"DRIVER={ODBC Driver 17 for SQL Server};"
            r"SERVER=LAPTOP-IUDORUJJ\SQLEXPRESS;"
            r"DATABASE=IN450;"
            r"Trusted_Connection=yes;"        
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

