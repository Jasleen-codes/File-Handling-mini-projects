import os

file = "students.txt"

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll No: ")
        name = input("Name: ")
        marks = int(input("Marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"

        with open(file, "a") as f:
            f.write(f"{roll},{name},{marks},{grade}\n")

        print("Record Added!")

    elif choice == "2":
        if os.path.exists(file):
            with open(file, "r") as f:
                print("\nStudent Records")
                print("----------------")
                print(f.read())
        else:
            print("No records found.")

    elif choice == "3":
        roll = input("Enter Roll No: ")
        found = False

        if os.path.exists(file):
            with open(file, "r") as f:
                for line in f:
                    r, n, m, g = line.strip().split(",")
                    if r == roll:
                        print(f"Roll: {r}")
                        print(f"Name: {n}")
                        print(f"Marks: {m}")
                        print(f"Grade: {g}")
                        found = True
                        break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")