def write():
    import csv
    f=open('student.csv','w')
    writer=csv.writer(f, delimiter=',')
    fields=['no','name','stream','marks']
    writer.writerow(fields)
    r=int(input('no'))
    n=input('name')
    s=input('stream')
    m=input('marks')
    writer.writerow([r,n,s,m])
    f.close()
def writeall():
    import csv
    f=open('student.csv','w')
    writeall=csv.writer(f)
    fields=['no','name','stream','marks']
    writeall.writerow(fields)
    d='y'
    lst=[]
    while d=='y':
        r=int(input('no'))
        n=input('name')
        s=input('stream')
        m=input('marks')
        lst.append([r,n,s,m])
        d=input('enter y to continue adding rows')
    writeall.writerows(lst)
    f.close()
def display():
    import csv
    f=open('student.csv','r')
    robj=csv.reader(f)
    for i in robj:
        print(i)

import csv
c='y'
while c=='y':
    print('1. write a single row to csv')
    print('2. write all records in one single go onto the csv')
    print('3. display the contents of the csv file')
    ch=int(input('enter choice'))
    if ch==1:
        write()
    elif ch==2:
        writeall()
    elif ch==3:
        display()
    else:
        print('invalid entry')
    c=input('enter y to continue')
    
        
            
            
    
