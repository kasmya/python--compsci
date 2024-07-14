def lmove(lst,n):
    for i in lst:
        lst[i]=lst[i+n]
    print(lst)
a=[1,2,3,4,5]
lmove(a,2)
