'''
def Call(p=40,q=20):
	p=p+q
	q=p-q
	print(p,'@',q)
	return p
r=200
s=100
print(r,'@',s)
s=Call(s)
print(r,'@',s)

def Sum3(l):
    sum=0
    for i in l:
        if i%10==3:
            sum+=i
        else:
            continue
    print(sum)
l=[13,20,3]
Sum3(l)

def Lshift(Arr,n):
    x=Arr[n:]+Arr[:n]
    print(x)
Arr=[10,20,30,40,12,11]
n=2
Lshift(Arr,n)
'''
def display(L):
    for i in L:
        if i.isdigit:
            print(i*3)
        else:
            print(i+'#')
list1=['kb','11','0','k']
display(list1)
