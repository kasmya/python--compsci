a=input("Enter a number:")
list1=list(a)
d={}

for i in list1:
    key=i
    if key not in d:
        freq=list1.count(key)
        d[key]=freq

print (d)
