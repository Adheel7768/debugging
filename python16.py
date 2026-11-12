import matplotlib.pyplot as plt
students=[]
marks=[]
n=int(input("Enter the number of students: "))
for i in range (n):
    name=input("Enter student name: ")
    mark=int(input("Enter student mark: "))
    students.append(name)
    marks.append(mark)
plt.bar(students,marks,color='blue')

plt.title("student marks chart")
plt.xlabel("Students names")
plt.ylabel("Marks")

for i in range(len(marks)):
    plt.text(i,marks[i]+0.2,str(marks[i]),ha='center')

plt.ylim(0, 35)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()
