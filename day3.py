import numpy as np

data = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 92],
    [60, 65, 70]
])

student_average = np.mean(data, axis=1)
print("Average of each student:", student_average)

subject_average = np.mean(data, axis=0)
print("Average of each subject:", subject_average)

highest = np.max(data)
print("Highest mark:", highest)

students_above_80 = student_average > 80
print("Students with average above 80:", students_above_80)

shape = data.shape
print("Shape:", shape)

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Add: ",a+b)
print("Sub: ",a-b)
print("Mul: ",a*b)
print("Div: ",a/b)

data = np.array([10, 20, 30, 40, 50])

print("Data: ",data)
print("Shape: ",data.shape)
print("Size: ",data.size)
print("No of Dim: ",data.ndim)
print("Data type: ",data.dtype)
print("Numeric Operation: ",data*2)
