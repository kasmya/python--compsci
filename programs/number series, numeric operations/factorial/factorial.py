
num=int(input('enter your number-'))
factorial=1
if num<0:
    print('there is no factorial')
elif num==0:
    print('factorial is 1')
else:
    for i in range (1,num+1):
        factorial=factorial*i
print(factorial)
