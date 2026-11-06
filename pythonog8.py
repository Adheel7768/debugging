students={
    "Adheel":99,
    "hadhi":35,
    "jasim":40,
    "abhijith":38
}
print("students scoring above 75:")
for name, marks in students.items():
    if marks>75:
        print(name,"-",marks)
        