import csv

filename = "students.csv"

with open(filename, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students = list(reader)

average = sum(int(s["Assessment"]) for s in students) / len(students)
print(f"Average rating: {average:.2f}")

new_student = {"Name": "Emma", "Age": 39, "Assessment": 100}
with open(filename, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Assessment"])
    writer.writerow(new_student)
