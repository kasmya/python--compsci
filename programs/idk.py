n=int(input("Enter the number of terms:"))


for i in range(2,n+1):
sum1=sum1+((x**i)/i)
print("The sum of series is",round(sum1,2))