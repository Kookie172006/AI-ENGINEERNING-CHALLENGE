
name = input("Enter student name: ")

subjects = ["Python", "DBMS", "OS", "CN", "AI"]
marks = []

for subject in subjects:
    mark = int(input("Enter marks in " + subject + ": "))
    marks.append(mark)

total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)

if lowest >= 40:
    result = "Pass"
else:
    result = "Fail"

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

student = {
    "Name": name,
    "Marks": marks,
    "Total": total,
    "Average": average,
    "Highest": highest,
    "Lowest": lowest,
    "Result": result,
    "Grade": grade
}

print("\n----- Student Report -----")
print("Student:", student["Name"])

print("\nMarks:")
for i in range(5):
    print(subjects[i] + "-", student["Marks"][i])

print("\nTotal:", student["Total"])
print("Average:", student["Average"])
print("Highest:", student["Highest"])
print("Lowest:", student["Lowest"])
print("Result:", student["Result"])
print("Grade:", student["Grade"])