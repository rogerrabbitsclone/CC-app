import pyodbc
cnxn = pyodbc.connect('DRIVER={FileMaker ODBC};SERVER=108.254.144.123:5003;DATABASE=TBS;UID=Admin;PWD=admin')
cursor = cnxn.cursor()
cursor.execute("select publisher from dun")

row = cursor.fetchall()
if row:
    print row[2]
