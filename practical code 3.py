#question 1 (b)
nostd = int(input("enter number of students: "))  
result = {}  
for i in range(nostd):
    print("enter details", i+1)
    rollno = int(input("roll no: "))
    stdname = input("student name: ")
    marks = int(input("marks: "))
    result[rollno] = [stdname, marks]    
print(result)  
for student in result:
    if result[student][1] > 75:
        print("student who got more than 75 marks is",(result[student][0]))

