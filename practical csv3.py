def add():
    import csv
    f=open('furdata.csv','a',newline='')
    w=csv.writer(f)
    fid=int(input('enter furniture id'))
    fname=input('enter name')
    fprice=int(input('enter price'))
    lst=[fid,fname,fprice]
    w.writerow(lst)
    f.close()
def search():
    import csv
    f=open('furdata.csv','r',newline='')
    r=csv.reader(f)
    d=list(r)
    count=0
    if lst[2]<10000:
        count+=1   
    print(count)
    f.close()
add()
search()
    
