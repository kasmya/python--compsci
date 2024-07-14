num=int(input('enter number-'))

#to remove garbage value
rev=0
num2=num

while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
print('reverse number-',rev)



    
