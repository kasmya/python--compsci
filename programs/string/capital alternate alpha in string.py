str=input('enter string')
leng=len(str)
str2=''
for a in range(0,leng):
    if a%2==0:
        str2=str2+str[a].upper()
    else:
        str2=str2+str[a]
print(str2)

