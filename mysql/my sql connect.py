'''
import mysql.connector
conn=mysql.connector.connect (host='localhost',user='root',passwd='jungcock')
mycur=conn.cursor()
mycur.execute('create database telephonedir')
mycur.execute('show databases')
for x in mycur:
    print(x)
conn.close()
'''
import mysql.connector
conn=mysql.connector.connect (host='localhost',user='root',passwd='jungcock',database='telephonedir')
mycur=conn.cursor()
'''mycur.execute('use telephonedir')
mycur.execute('create table customer(cust_id int(5),cust_name varchar(40),tele_no varchar(15),date_of_reg date)')
mycur.execute('show tables')

mycur.execute('desc customer')

mycur.execute('insert into customer values(101, 'mr cp gupta',9812343134,'2018/01/21')')
mycur.execute('select * from customer')
'''
cid=int(input('enter customer id'))
name=input('enter name of customer')
t_num=input('enter telephone number')
dt=input('enter date of registration (year/mm/dd)')
qry='insert into customer (cust_id,cust_name,tele_no,date_of_reg)values(%s,%s,%s,%s)'
val=(cid,name,t_num,dt)
mycur.execute(qry,val)
conn.commit()
for x in mycur:
    print(x)
conn.close()
