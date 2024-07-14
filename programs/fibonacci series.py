n=int(input('enter limit-'))
x=0
y=1
z=1
print('fibonacci series/n')
print(x,y,end='')
while (z<=n):
    print(z,end='')
    x=y
    y=z
    z=x+y
