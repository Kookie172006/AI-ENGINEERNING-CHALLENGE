import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "department": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "marks": [85, 72, 91, 64, 78],
    "attendance": [90, 80, 95, 60, 85]
}

df = pd.DataFrame(data)

print("student data")
print(df)

print("\nfirst 5 rows")
print(df.head())

print("\ndataset information")
df.info()

print("\nstatistics")
print(df.describe())

average_marks = df["marks"].mean()

print("\naverage marks:", average_marks)

print("\nstudents scoring above 80")
print(df[df["marks"] > 80])

print("\nstudents with attendance below 75")
print(df[df["attendance"] < 75])

print("\naverage marks by department")
print(df.groupby("department")["marks"].mean())

df["result"] = df["marks"] >= 40

df["performance"] = "Needs Improvement"

df.loc[(df["marks"] >= 70) & (df["marks"] < 85), "performance"] = "Good"

df.loc[df["marks"] >= 85, "performance"] = "Excellent"

print("\nupdated student data")
print(df)

print("\nstudents sorted by marks")
print(df.sort_values("marks", ascending=False))

