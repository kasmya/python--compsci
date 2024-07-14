def listchange(arr):
    l=len(arr)
    for i in range(l):
        if arr[i]%2==0:
            arr[i]=10
        else:
            arr[i]=arr[i]*5
    print(arr)
arr=[10,20,23,45]
listchange(arr)
