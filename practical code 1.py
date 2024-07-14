print("menu")  
print("1. find the factorial of a number:")  
print("2. check whether a number is palindrome or not")  
print("3. exit")  
choice = int(input("Enter your Choice: "))  
if choice==1: #question 1 (a) (i)
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
elif choice==2: #question 1 (a) (ii)
    print ("a number is palindrome or not")
    a=int(input("enter number: "))
    num=a
    rev=0
    while num>0:
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if rev==a:
        print ("The reverse of,",a,"is",rev,"therefore it is a palindrome number")
    else:
        print ("The reverse of,",a,"is",rev,"therefore it is not a palindrome number") 
elif choice==3: #question 1 (a) (iii)
    print('exit')



