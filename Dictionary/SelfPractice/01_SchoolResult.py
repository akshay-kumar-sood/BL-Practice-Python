# PROG 1: School Result

# Write The Code Here
# PROG 1: School Result

import random


# Function to calculate grade based on percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# Function to give remarks based on grade
def get_remarks(grade):
    if grade == "F":
        return "Failed, work hard to do better next time"
    else:
        return "Congratulations!, Passed Successfully"


# List to store all students
students = []


# Create data for 5 students
for i in range(1, 6):

    # Generate random marks out of 50
    physics = round(random.uniform(0, 50), 1)
    chemistry = round(random.uniform(0, 50), 1)
    maths = round(random.uniform(0, 50), 1)

    # Generate random gender
    gender = random.choice(["M", "F"])

    # Generate random attendance
    attendance = random.randint(0, 100)

    # Calculate total marks
    total = physics + chemistry + maths

    # Calculate percentage
    percentage = round((total / 150) * 100, 2)

    # Calculate grade
    grade = get_grade(percentage)

    # Get remarks
    remarks = get_remarks(grade)

    # Store student data in dictionary
    student = {
        "Name": f"Student{i}",
        "Gender": gender,
        "Marks": {
            "Physics": physics,
            "Chemistry": chemistry,
            "Maths": maths
        },
        "Attendance": attendance,
        "Total": round(total, 1),
        "Percentage": percentage,
        "Grade": grade,
        "Remarks": remarks
    }

    # Add student dictionary to list
    students.append(student)


# Ask user how results should be displayed
choice = input(
    "Enter 'grade' to display results by grade or "
    "'percentage' to display results by percentage: "
).lower()


# Sort students
if choice == "grade":
    students.sort(key=lambda student: student["Grade"])

elif choice == "percentage":
    students.sort(key=lambda student: student["Percentage"], reverse=True)

else:
    print("Invalid choice")


# Print results
if choice == "grade" or choice == "percentage":

    for student in students:

        print("-" * 50)

        print(f"Name: {student['Name']}")
        print(f"Gender: {student['Gender']}")

        print("Marks:")
        print(f"- Physics: {student['Marks']['Physics']}")
        print(f"- Chemistry: {student['Marks']['Chemistry']}")
        print(f"- Maths: {student['Marks']['Maths']}")

        print(f"Attendance: {student['Attendance']}")

        print(f"Total Marks: {student['Total']}/150")
        print(f"Percentage Marks: {student['Percentage']}%")

        print(f"Attendance: {student['Attendance']}")
        print(f"Grade: {student['Grade']}")
        print(f"Remarks: {student['Remarks']}")