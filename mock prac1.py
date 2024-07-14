import pickle
def write():
    a=open('shoes.dat','ab')
    ch='y'
    while ch=='y':
        r=int(input('enter id'))
        n=input('enter name')
        b=input('enter brand')
        t=input('enter type')
        p=int(input('enter price'))
        data=[r,n,b,t,p]
        pickle.dump(data,a)
        ch=input('enter y to continue adding')
    a.close()

def display():
    a=open('shoes.dat','rb')
    try:
        while True:
            rec=pickle.load(a)
            print(rec)
    except:
        a.close()

def search(id):
    a=open('shoes.dat','rb')
    try:
        while True:
            rec=pickle.load(a)
            if rec[0]==id:
                print(rec[1])
    except:
        a.close()
        
ch=int(input('enter choice'))
if ch==1:
    write()
elif ch==2:
    display()
elif ch==3:
    id=int(input('enter id'))
    search(id)
elif ch==4:
    print('exit')
    
    
