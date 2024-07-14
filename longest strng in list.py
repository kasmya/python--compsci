l=[]
e1=input('enter no. of elements')
for i in e1:
    l1=input('enter element')
    l+=l1[i]
max=l[0]
for a in l:
    if len(max)>len(l[a]):
        max=a
print(l[a])
