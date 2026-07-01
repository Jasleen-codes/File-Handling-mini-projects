import random
import string

# password generator 
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_password(password, filename="passwords.txt"):
    with open(filename, "a") as f:
        f.write(password + "\n")
    print("Password generated and saved:", password)

# func password validator
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(ch.isupper() for ch in password):
        return False
    if not any(ch.islower() for ch in password):
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    if not any(ch in string.punctuation for ch in password):
        return False
    return True

def validate_from_file(filename="passwords.txt"):
    try:
        with open(filename, "r") as f:
            for line in f:
                pwd = line.strip()
                print(pwd, "->", "Valid" if validate_password(pwd) else "Invalid")
    except FileNotFoundError:
        print("No password file found. Generate some passwords first!")

# 

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Generate Password")
        print("2. Validate Passwords from File")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            pwd = generate_password(length)
            save_password(pwd)
        elif choice == "2":
            validate_from_file()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
if __name__ == "__main__":
    main()
