# PROG 6: To Generate School Report Using List

# Write The Code Here
import random

TOTAL_SUBJECT_MARKS = 50

students = [
    "Olivia", "Emma", "Liam", "Noah", "Ava",
    "Sophia", "James", "Lucas", "Mia", "Ethan"
]

physics_marks = []
chemistry_marks = []
maths_marks = []

# Generate random marks for 10 students
for student in students:
    physics_marks.append(random.randint(0, 50))
    chemistry_marks.append(random.randint(0, 50))
    maths_marks.append(random.randint(0, 50))


name = input("Enter name of student: ")

if name in students:

    index = students.index(name)

    physics = physics_marks[index]
    chemistry = chemistry_marks[index]
    maths = maths_marks[index]

    physics_percentage = (physics / TOTAL_SUBJECT_MARKS) * 100
    chemistry_percentage = (chemistry / TOTAL_SUBJECT_MARKS) * 100
    maths_percentage = (maths / TOTAL_SUBJECT_MARKS) * 100

    total_marks = physics + chemistry + maths
    total_percentage = (total_marks / 150) * 100

    print("\nNew School Of Learning - Class XI -", name)
    print("-----------------------------------------------------------------------")
    print("Subject\t\tTotal Marks\tMarks Obtained\tPercentage")
    print("-----------------------------------------------------------------------")
    print("Physics\t\t", 50, "\t\t", physics, "\t\t", round(physics_percentage, 2))
    print("Chemistry\t", 50, "\t\t", chemistry, "\t\t", round(chemistry_percentage, 2))
    print("Mathematics\t", 50, "\t\t", maths, "\t\t", round(maths_percentage, 2))
    print("-----------------------------------------------------------------------")
    print("Total\t\t", 150, "\t\t", total_marks, "\t\t", round(total_percentage, 2))
    print("-----------------------------------------------------------------------")

else:
    print("Student not found")