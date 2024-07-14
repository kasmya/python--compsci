import pickle
def write():
    a=open('studata.dat','ab')
    ch='y'
    while ch=='y':
        r=int(input('enter roll number'))
        n=input('enter name')
        data=[r,n]
        pickle.dump(data,a)
        ch=input('enter y to continue adding')
    a.close()
write()
def read():
    a=open('studata.dat','rb')
    try:
        while True:
            rec=pickle.load(a)
            print(rec)
    except:
        a.close()
read()
def searchrno(rno):
    a=open('studata.dat','rb')
    try:
        while True:
            rec=pickle.load(a)
            if rec[0]==rno:
                print(rec[1])
    except:
        a.close()
searchrno(11)
