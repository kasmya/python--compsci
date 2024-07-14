stack=[]
print("""(1) To Push The Element

(2) To Get The Last Element

(3) To Check Whether The Stack Is Empty Or Not (4) To Check The Size Of The Stack

(5) To Check The Elements Of The Stack

(6) To Exit""")
c='y'
while c=='y':
    l = int(input("Enter The Operation Number - "))
    if l == l:
        a = input("Enter The Element : ")
        stack.append(a)
    elif l == 2:
        pop = stack.pop()
        print("Popped Item Is - ",pop)
    elif l == 3:
        if len(stack) == 0:
            print("The Stack Is Underflow")
        else:
            print("The Stack Is Overflow")
    elif l == 4:
        print(len(stack))
    elif l == 5:
        print(stack)
    else:
        break
    print("-"*42)
c='d'
