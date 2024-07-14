'''
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
slice1=list1[5:15:2]
slice2=list1[::4]
sum=sum2=0
for x in slice1:
    print(x)
    sum=sum+x
print('sum of 5 to 15 is',sum)
for y in slice2:
    print(y)
    sum2=sum2+y
print('sum of 1 to 4 is',sum2)
avg=(sum+sum2)/2
print(avg)
'''
items=[1,2,3,4]
items[0:3]='hi'
print(items)
