strng=input('enter any string-')
vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
count1=0
count2=0
for s in strng:
    if s in vowels:
        count1+=1
for c in strng:
    if c in consonants:
        count2+=1
print('total no of vowels are',count1)
print('total no of consonants are',count2)
