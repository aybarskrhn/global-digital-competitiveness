def menu_goster():
    print("\nWelcome!")
    print("1 - Add new user")
    print("2 - Show all users")
    print("3 - Exit")
def add_user():
    print("Adding a new user...")
    name = input("Enter the name: ")
    surname = input("Enter the surname: ")
    age = input("Enter the age: ")
    if not age.isdigit():
        print("Invalid age. Please enter a number.")
        return
    university = input("Enter the university: ")
    with open("kullanicilar.txt", "a", encoding="utf-8") as dosya:
        dosya.write("-----\n")
        dosya.write(f"Name: {name}\n")
        dosya.write(f"Surname: {surname}\n")
        dosya.write(f"Age: {age}\n")
        dosya.write(f"University: {university}\n")
        dosya.write("-----\n\n")
        print("User added successfully!")
def show_users():
    print("Showing all users...")
    try:
        with open("kullanicilar.txt", "r", encoding="utf-8") as dosya:
            content = dosya.read()
            if content.strip() == "":
                print("No users found.")
            else:
                print("\n Saved Users:\n")
                print(content)
    except FileNotFoundError:
        print("No users found.")
while True:
    menu_goster()
    choice = input("Please select an option: ")
    if choice == "1":
        add_user()
    elif choice == "2": 
        show_users()
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again.")


# This code is a simple menu-driven program that allows the user to add new users, show all users, or exit the program.
