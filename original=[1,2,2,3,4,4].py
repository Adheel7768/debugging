original=[1,2,2,3,4,4]
unique=[]
for item in original:
    if item not in unique:
        unique.append(item)
print("list without duplicate:",unique)
