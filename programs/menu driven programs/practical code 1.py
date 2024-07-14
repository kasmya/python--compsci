#to calculate the day of year
day=int(input('enter date-'))
#input taken from the user to predict the day of the year
month=input('enter month-')
if (month=='january'):
    dayofyear=day
elif (month=='feburary'):
    dayofyear=30+day
#for making calculations easier no of days in each month is taken as 30
elif (month=='march'):
    dayofyear=60+day
#30 is being added after every month as 30 days of the year have passed since then
elif (month=='april'):
    dayofyear=90+day
elif (month=='may'):
    dayofyear=120+day
elif (month=='june'):
    dayofyear=150+day
elif (month=='july'):
    dayofyear=180+day
elif (month=='august'):
    dayofyear=210+day
elif (month=='september'):
    dayofyear=240+day
elif (month=='october'):
    dayofyear=270+day
elif (month=='november'):
    dayofyear=300+day
elif (month=='december'):
    dayofyear=330+day
else:
    print('month entered is not valid')
print('the day of the year is',dayofyear)
#output given to the user, day of the year is predicted
    
