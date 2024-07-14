import mysql.connector
con=mysql.connector.connect (host='localhost',user='root',passwd='jungcock')
mcon=con.cursor()
mcon.execute('show databases')

for x in mcon:
    print(x)
