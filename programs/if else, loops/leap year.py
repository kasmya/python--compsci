year=int(input('enter a year-'))#to check if a year is a leap year
if year%100==0:
    if year%400==0:
        print('year is a leap year')
    else:
        print('not a leap year')
elif year%4==0:
    print('year is a leap year')
else:
    print('year is not a leap year')
