# Self Practice LOng COde

# Menu Based School Report

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    else:
        return "F"


def result(name, phy, chem, maths, max_marks=100, type="p"):
    total = phy + chem + maths

    print(f"\nNew School Of Learning - Class XI - {name}")

    if type == "p":
        print("-" * 73)
        print("|     Subject     |   Total Marks   | Marks Obtained  |   Percentage    |")
        print("-" * 73)
        print(f"|     Physics     |       {max_marks}       |       {phy}        | {phy/max_marks*100:.2f}%          |")
        print(f"|    Chemistry    |       {max_marks}       |       {chem}        | {chem/max_marks*100:.2f}%          |")
        print(f"|   Mathematics   |       {max_marks}       |       {maths}        | {maths/max_marks*100:.2f}%          |")
        print("-" * 73)
        print(f"|      Total      |       {max_marks*3}       |       {total}       | {total/(max_marks*3)*100:.2f}%          |")
        print("-" * 73)

    elif type == "g":
        print("-" * 32)
        print("|     Subject     |   Grade    |")
        print("-" * 32)
        print(f"|     Physics     |     {grade(phy/max_marks*100):<3}    |")
        print(f"|    Chemistry    |     {grade(chem/max_marks*100):<3}    |")
        print(f"|   Mathematics   |     {grade(maths/max_marks*100):<3}    |")
        print("-" * 32)
        print(f"|      Total      |     {grade(total/(max_marks*3)*100):<3}    |")
        print("-" * 32)


name = input("Enter student's name: ")
max_marks = int(input("Enter max marks per subject: "))
phy = int(input("Enter physics marks: "))
chem = int(input("Enter chemistry marks: "))
maths = int(input("Enter maths marks: "))
type = input("Enter computation type (g for grades, p for percentage): ")

result(name, phy, chem, maths, max_marks, type)