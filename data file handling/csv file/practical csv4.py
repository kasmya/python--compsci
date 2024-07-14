def add_item():
    import csv
    f=open('stationary.csv','a',newline='')
    w=csv.writer(f)
    item_id=int(input('enter item id'))
    item_name=input('enter item name')
    item_price=int(input('enter price'))
    lst=[item_id,item_name,item_price]
    w.writerow(lst)
    f.close()
def count():
    import csv
    f=open('stationary.csv','r',newline='')
    r=csv.reader(f)
    l=list(r)
    print(len(l))
    f.close()
add_item()
count()
