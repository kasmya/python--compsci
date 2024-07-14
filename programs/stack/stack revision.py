#stack implementation
'''s=[]
c='y'
while c=='y':
    print('select a choice')
    print('1. PUSH')
    print('2. POP')
    print('3. DISPLAY')
    choice=int(input('enter your choice number'))
    if choice==1:
        num=int(input('enter number of elements to be added'))
        for i in range(0,num):
            a=input('enter element')
            s.append(a)
        print(s)
    elif choice==2:
        if s==[]:
            print('stack underflow')
        else:
            s.pop()
            print('deleted element is',s.pop())
            print(s)
    elif choice==3:
        l=len(s)
        for i in range(l-1,-1,-1):
            print(s[i])
    else:
        print('wrong output')
    c=input('enter y to continue')
'''
#similar ques
employee=[]
c='y'
while c=='y':
    print('select a choice')
    print('1. PUSH')
    print('2. POP')
    print('3. DISPLAY')
    choice=int(input('enter your choice number'))
    if choice==1:
        enum=int(input('enter employee number'))
        ename=input('enter employee name')
        ed=(enum,ename)
        employee.append(ed)
    elif choice==2:
        if employee==[]:
            print ('stack underflow')
        else:
            enum,ename=employee.pop()
            print('deleted elements are',enum,ename)
    elif choice==3:
        i=len(employee)
        while i>0:
            print(employee[i-1])
            i=i-1
        else:
            print('empty stack')
    else:
        print('wrong input')
    c=input('enter y to continue')
        

    
