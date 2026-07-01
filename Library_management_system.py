# Library management system 
import os

file = "library.txt"

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Book Title: ")
        author = input("Author: ")

        with open(file, "a") as f:
            f.write(f"{book_id},{title},{author}\n")

        print("Book Added Successfully!")

    elif choice == "2":
        if os.path.exists(file):
            with open(file, "r") as f:
                print("\nBook Records")
                print("-------------------------")
                print(f.read())
        else:
            print("No books available.")

    elif choice == "3":
        search = input("Enter Book ID: ")
        found = False

        if os.path.exists(file):
            with open(file, "r") as f:
                for line in f:
                    bid, title, author = line.strip().split(",")
                    if bid == search:
                        print("\nBook Found")
                        print("Book ID :", bid)
                        print("Title   :", title)
                        print("Author  :", author)
                        found = True
                        break

        if not found:
            print("Book not found.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")