import pyodbc
#as long as the ports are forwarded on the router, you can do this remotly. 
cnxn = pyodbc.connect('DRIVER={FileMaker ODBC};SERVER=108.254.144.23:2399;DATABASE=TBS3;UID=rocket;PWD=rocket')
pyodbc.connect
cursor = cnxn.cursor()
#to find the table name, open the database in filemaker VIA openremote.
#then go: file->manage->database. in the "Table" tab you can change the table name
#filemakers "fields" are SQLs "columns"
#IE: cursor.execute("select publisher from tobesentsent") is selecting the 'publisher' column from the 'tobesent' table
#tables cannot have spaces due to pyodbc limitations
cursor.execute("select publisher from tobesentsent")

row = cursor.fetchall()
if row:
    print row[3]
