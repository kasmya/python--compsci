#shoes binary
import pickle
while True:
    print('''
1. Add record
2. Display record
3. Search record
4. Exit''')
    ch=int(input('enter choice'))
    lst=[]
    if ch==1:
        f=open('shoes.dat','wb')
        s_id=int(input('enter id'))
        name=input('enter name')
        brand=input('enter brand')
        typ=input('enter type')
        price=int(input('enter price'))
        lst=[s_id,name,brand,typ,price]
        pickle.dump(lst,f)
        print('record is added')
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
        si=int(input('enter id'))
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
        print('invalid choice')
                        
                
