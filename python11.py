numbers=[10,20,30,40,50]

key=int(input("Enter a number to search: "))

found=False

for i in range(len(numbers)):
    if numbers[i]==key:
        print("element found at position",i+1)
        found=True
        break

    if found==False:
        print("element not found")
        
