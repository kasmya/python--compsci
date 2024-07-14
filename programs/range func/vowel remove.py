x=input('enter string')
v='a,e,i,o,u'
c=''
for i in range(len(x)):
    if x[i] not in v:
        c=c+x[i]
print ("without vowels",c)
