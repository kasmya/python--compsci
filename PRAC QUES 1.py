
import pickle
def add():
 f=open("shoes.dat","wb")
 a = int (input("Enter Shoe id: "))
 b=input("Name: ")
 z = input("Brand: ")
 s = input("Type: ")
 c = int(input("Price: "))
 rec = [a,b,z,s,c]
 pickle.dump( rec, f )
 f.close()


def read():
    f= open("shoes.dat","rb")
    x = pickle.load(f)
    print(x)
    f.close()
def search():
    f = open("shoes.dat","rb")
    a = pickle.load(f)
    n = input("Enter content to be searched: ")
    for i in a:
        if i[0] == n:
            print(i)
    f.close()

c='y'
while c=='y':
    print('1. Add data')
    print('2 Display')
    print('3 Search')
    ch=int(input('enter choice: '))
    if ch==1:
        add()
    elif ch==2:
        read()
    elif ch==3:
        search
    else:
        print('invalid entry')
    c=input('enter y to continue')
