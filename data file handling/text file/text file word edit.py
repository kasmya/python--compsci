def changeword():
    a=open('1thingaboutme.txt','r')
    text=a.read()
    print(text.replace('he','she'))
    a.close()
changeword()

'''
    lines=a.readlines()
    for i in lines:
        words=i.split()
        for j in words:
            if j=='he':
                j='she'
            print(i,sep='')
changeword()
'''
