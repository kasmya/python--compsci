import pickle
def countsal():
    a=open('emp1.dat','rb')
    b=pickle.load(a)
    c=pickle.dump([11,'kasmya',2000000])
    count=0
    for i in b:
        if b[2]>20000:
            print(b[0],b[1],b[2],sep='\n')
            count+=1
        else:
            continue
countsal()
