def count():
    f=open('data.csv','r',newline='')
    r=csv.reader(f)
    d=list(r)
    print('number of records present',len(d))
    
