import csv
def add():
    f=open('record.csv','a',newline='')
    write=csv.writer(f)
    empid=int(input('enter employee id'))
    name=input('enter name')
    mobile=int(input('enter mobile number'))
    row=[empid,name,mobile]
    write.writerow(row)
    f.close()
def countr():
    f=open('record.csv','r',newline='')
    records=csv.reader(f)
    a=list(records)
    print('number of records in csv file are',len(a))
    f.close()
add()
add()
countr()
