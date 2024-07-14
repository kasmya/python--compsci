#b. Observe the following code and fill in the given blanks as directed:
import mysql.connector as mycon
cn=mycon.connect(host="localhost",user="root",passwd="jungcock",database="Bangalore") #statement1
cr=cn.cursor()  #statement 2
cust_id=int(input("Enter ID to Update: "))
cust_name=input("Enter Customer Name (New): ")
city=input("Enter city name (new): ")
ba=float(input("Enter Bill Amount (New): "))
mno=input("Enter Mobile No.(New): ")
statement="Update customer set CustomerName=%s,City=%s,BillAmt=%s, MobileNo=%s where CustomerID=%s "
values=[cust_name,city,ba,mno,cust_id]
cr.execute(statement,values)    #statement3
cn.commit()    #statement 4
cn.close()



