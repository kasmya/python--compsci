def Lshift(arr,n):
    l=len(arr)
    beg=arr[0]
    for i in range(0,n):
        for i in range(0,l-1):
            arr[i]=arr[i+1]
        arr[l-1]=arr[0]
    print(arr)
arr=[1,2,3,4]
Lshift(arr,2)
    
