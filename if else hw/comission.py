#to calculate commission and salary of a salesman
monthly_sale=int(input('enter monthly sale-'))
if monthly_sale>500000:
    commission=(monthly_sale*10)/100
else:
    commission=(monthly_sale*5)/100
print ('commission is', commission, 'salary is', monthly_sale+commission)

