'''
for i in range (1,5):
    for j in range (1,i+1):
        print('*',end='')
    print()


n=int(input('enter no'))
for r in range (1,n+1):
    for s in range (1,r+1):
        print ('*', end='')
    print()
'''

n=int(input('enter no'))
for a in range (n,0,-1):
    for b in range (a,0,-1):
        print ('*', end='')
    print()
