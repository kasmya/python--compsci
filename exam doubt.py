numb=int(input('enter a number'))
tem=numb
rev=0
while(numb>0):
    dig=numb%10
    rev=rev*10+dig
    numb=numb//10
if tem==rev:
    print('is palindrome')
else:
    print('is not palindrome')
