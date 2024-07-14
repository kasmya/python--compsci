vowels=['a','e','i','o','u']
s=[]
word=input('enter word')
for i in word:
    if i in vowels:
        if i not in s:
            s.append(i)
print(s)

