import pickle
m='y'
while m=='y':
    print('1. add record')
    print('2. display records')
    print('3. search record')
    print('4. exit')
    ch=int(input('enter choice'))
    if ch==1:
        try:
            lst=[]
            a=open('shoes.dat','wb')
            s_id=int(input('enter id'))
            name=input('enter name')
            brand=input('enter brand')
            typee=input('enter type')
            price=int(input('enter price'))
            rec=[s_id,name,brand,typee,price]
            pickle.dump(a,rec)
            a.close()
        except EOFError:
                a.close()
        m=input('enter y to continue menu driven program')
        
    elif ch==2:
        a=open('shoes.dat','rb')
        b=pickle.load(a)
        for i in b:
            print(i)
        m=input('enter y to continue menu driven program')
            
    elif ch==3:
        a=open('shoes.dat','r')
        b=pickle.load(a)
        s=int(input('enter id to search record'))
        if s==b[0]:
            print('record found')
            print(b[0],b[1],b[2],b[3],b[4])
        else:
            print('record not found')
        m=input('enter y to continue menu driven program')
            
    elif ch==4:
        print('end of program')
        break
        
    else:
        print('invalid choice')
        break
        
       
    
    
        
        
        
    
