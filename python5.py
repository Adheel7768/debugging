text=input("enter a string:")
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count+=1
print("number of vowels=",count)