'''
n=int(input('enter no of subjects'))
tuple1=()
for i in range(n):
    a=input('enter subject')
    tuple1=tuple1+(a,)
print(tuple1)
'''
n=int(input('enter no'))
tuple1=()
for i in range(n):
    a=input('enter name')
    b=int(input('enter roll no'))
    c=input('enter subject')
    tuple2=(a,)+(b,)+(c,)
    tuple1=tuple1+(tuple2,)
print(tuple1)
