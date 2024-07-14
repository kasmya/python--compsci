#shoes binary
import pickle
while True:
    print('''
1. Add record
2. Display record
3. Search recordimport pickle''')

def insertRec():
    doctor_id = int(input('Enter doctor id:'))
    doctor_name = input('Enter Name:')
    hospital_id = int(input('Enter hosptial id:'))
    joining_date=input("Enter date:")
    speciality=input("Enter speciality:")
    salary=float(input("Enter Salary:"))

    rec = [doctor_id,doctor_name,hospital_id,joining_date,speciality,salary]

    f = open('hospital.dat','ab')
    pickle.dump(rec,f)
    f.close()


def readRec():
    f = open('hospital.dat','rb')
    while True:
        try:
            rec = pickle.load(f)
            print(rec)
        except EOFError:
            break
    f.close()


def updaterec():
    f = open('hospital.dat','rb')
    r1 = []
    while True:
        try:
            r = pickle.load(f)
            r1.append(r)
        except EOFError:
            break
    f.close()
    d_id=int(input("Enter doctor id to update:"))
    if d_id in r1:
        doctor_name = input('Enter new Name:')
        hospital_id = int(input('Enter new hosptial id:'))
        joining_date=input("Enter new date:")
        speciality=input("Enter new speciality:")
        salary=float(input("Enter new Salary:"))
        for i in range (len(r1)):
            if r1[i][0]==d_id:
                r1[i][1] = doctor_name
                r1[i][2]=hospital_id
                r1[i][3]=joining_date
                r1[i][4]=speciality
                r1[i][5]=salary
        f = open('hospital.dat','wb')
        for x in r1:
            pickle.dump(x,f)
        f.close()
    else:
        print("Record not found...")

def menu():
    while True:
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
                        
                
