numbers=list(map(int,input("enter numbers:").split()))
unique_numbers=list(set(numbers))
unique_numbers.sort()
if len(unique_numbers)>=2:
    print("second largest number:",unique_numbers[-2])
else:
    print("second largest number does not exist")
    