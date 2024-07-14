import mysql.connector as mycon
cn=mycon.connect(host='localhost',user='root',passwd='jungcock',database='lol') # Statement 1
cr=cn.cursor() # Statemen 2
cust_id=int(input('Enter ID:'))
cust_name=input('Enter Customer Name:')
city=input('Enter City:')
ba=float(input('Enter Bill Amount:'))
mno=input('Enter Mobile No.:')
cr.execute('insert into customer values({},"{}","{}",{},"{}")'.format(cust_id, cust_name, city, ba,mno))
cn.commit() # Statement 4
