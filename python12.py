numbers=[10, 20, 30, 40, 50,60,70]

key=int(input("enter the element to search:"))

low=0
high=len(numbers)-1
found=False

while low<=high:
    mid=(low+high)//2

    if numbers[mid]==key:
        print("element found at index:", mid+1)
        found=True
        break

    elif key<numbers[mid]:
          high=mid-1
    else:
         low=mid+1
if found==False:
    print("element not found")
