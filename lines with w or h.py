def cwh():
    a=open('Country.txt','r')
    b=a.readlines()
    count1=0
    count2=0
    for i in b:
        if i[0]=='w' or i[0]=='W':
            count1+=1
        elif i[0]=='h' or i[0]=='H':
            count2+=1
        else:
            continue
    print('W or w:',count1)
    print('H or h:',count2)
    a.close()
cwh()
