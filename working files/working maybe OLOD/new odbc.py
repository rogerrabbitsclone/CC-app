import pyodbc
pyodbc.connect(DRIVER="[FileMaker ODBC]", SERVER="192.168.1.113", DSN="TBS", UID="itstaff", PWD="5901c") 
connection = pyodbc.connect(DSN)
cursor = connection.cursor()

cursor.execute('select * from "Vehicle Faults"')
rows = cursor.fetchall()

for x in rows:
    print x
