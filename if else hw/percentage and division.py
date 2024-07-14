#to calculate total percentage and division of a student
subject1=int(input('enter marks of subject1-'))
subject2=int(input('enter marks of subject2-'))
subject3=int(input('enter marks of subject3-'))
subject4=int(input('enter marks of subject4-'))
subject5=int(input('enter marks of subject5-'))
percentage=(subject1+subject2+subject3+subject4+subject5)/500*100
print(percentage)
if percentage>=60:
    print('first division')
elif percentage>=45:
    print('second division')
elif percentage>=33:
    print('third division')
else:
    print('fail')
    
