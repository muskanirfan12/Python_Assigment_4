import csv

# Store in CSV
with open("attendance.csv", "a", newline="") as file:
    writer = csv.writer(file)
    student_info = input("Enter student information: ")
    timestamp = input("Enter timestamp: ")
    writer.writerow([student_info, timestamp])
    print("Attendance successfully recorded in CSV!")
