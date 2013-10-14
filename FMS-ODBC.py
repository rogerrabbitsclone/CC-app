import pyodbc
cnxn = pyodbc.connect('DRIVER={FileMaker ODBC};SERVER=192.168.1.113:5003;DATABASE=TBS;UID=itstaff;PWD=5901c')
pyodbc.connect
cursor = cnxn.cursor()
cursor.execute("select publisher from 2013 - summer.fp7")

row = cursor.fetchall()
if row:
    print row[3]
