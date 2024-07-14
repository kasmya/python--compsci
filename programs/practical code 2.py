n=int(input("enter number-"))#input is being taken from the user
rev=0 #has been taken as zero to ensure that the grabadge value is 0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("reverse is-",rev)#output is given to the user, the number given by the user is reversed
    
