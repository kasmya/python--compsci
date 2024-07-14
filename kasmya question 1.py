#a. Write a menu driven program to perform following operations into a binary file shoes.dat
import pickle
while True:
    print('''
    1. Add record
    2. Display records
    3. Search records
    4. Exit''')
    ch=int(input('Enter choice'))
    rec=[]
    if ch==1:
        f=open('shoes.dat','wb')
        s_id=int(input('Enter shoe id'))
        name=input('Enter shoe name')
        brand=input('Enter brand')
        typ=input('Enter type')
        price=int(input('Enter price'))
        rec=[s_id,name,brand,typ,price]
        pickle.dump(rec,f)
        print('Record added')
        f.close()
    elif ch==2:
        f=open('shoes.dat','rb')
        try:
            a=pickle.load(f)
            print(a)
        except:
            break
        f.close()
    elif ch==3:
        f=open('shoes.dat','rb')
        a=pickle.load(f)
        si=int(input('Enter shoe id'))
        found=0
        for i in a:
            if i==si:
                print('record found')
                print(a[0],a[1],a[2],a[3],a[4])
                found=1
        if found==0:
            print('record not found')
        f.close()
    elif ch==4:
        break
    else:
        print('Invalid choice')
                        
                


               
            
        
    
