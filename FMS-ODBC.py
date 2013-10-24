import pyodbc
cnxn = pyodbc.connect('DRIVER={FileMaker ODBC};SERVER=192.168.1.113:2399;DATABASE=TBS3;UID=rocket;PWD=rocket')
pyodbc.connect
cursor = cnxn.cursor()
#to find the table name, open the database in filemaker VIA openremote.
#then go: file->manage->database. in the "Table" tab you can change the table name
#filemakers "fields" are SQLs "columns"
cursor.execute("select publisher from tobesentsent")

row = cursor.fetchall()
if row:
    print row[3]
