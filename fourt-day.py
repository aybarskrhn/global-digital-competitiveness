import csv 
def menu():
    print("\n Welcome!") 
    print("1 - Add new user")
    print("2 - Show all users")
    print("3 - Exit")
    print("4 - Show statistics")
def add_user():
    print("Adding a new user...")
    name = input("Enter the name: ")
    surname = input("Enter the surname: ")
    age = input("Enter the age: ")
    if not age.isdigit():
        print("Invalid age. Please enter a number.")
        return
    university = input("Enter the university: ")
    with open("kullanicilar.csv", "a", newline='', encoding="utf-8") as dosya:
        writer = csv.writer(dosya)
        writer.writerow([name, surname, age, university])
        print("User added successfully!")
def show_users():
    print("Showing all users...")
    try:
        with open("kullanicilar.csv", "r", encoding="utf-8") as dosya:
            reader = csv.reader(dosya)
            content = list(reader)
            if not content:
                print("No users found.")
            else:
                print("\n Saved Users:\n")
                for row in content:
                    print(f"Name: {row[0]}, Surname: {row[1]}, Age: {row[2]}, University: {row[3]}")
    except FileNotFoundError:
        print("No users found.")

def add_user_csv():
    print("Adding a new user to CSV...")
    name = input("Enter the name: ")
    surname = input("Enter the surname: ")
    age = input("Enter the age: ")
    university = input("Enter the university: ")

    with open("kullanicilar.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, age, university])  # ← burayı sen tamamla!

    print("User added to CSV successfully!")
def show_statistics():
    try:
        with open("kullanicilar.csv", "r", encoding="utf-8") as dosya:
            reader = csv.reader(dosya)
            users = list(reader)

            if not users:
                print("No users to analyze.")
                return

            ages = []
            universities = []

            for row in users:
                if row[2].isdigit():
                    ages.append(int(row[2]))
                universities.append(row[3])

            total_users = len(users)
            average_age = sum(ages) / len(ages) if ages else 0

            most_common_uni = max(set(universities), key=universities.count)

            print(f"\n📊 Total users: {total_users}")
            print(f"📈 Average age: {average_age:.2f}")
            print(f"🏫 Most common university: {most_common_uni}")

    except FileNotFoundError:
        print("No data file found.")

while True:
    menu()
    choice = input("Please select an option: ")
    if choice == "1":
        add_user()
    elif choice == "2": 
        show_users()
    elif choice == "3":
        print("Exiting the program...")
    elif choice == "4":
        show_statistics()    
        break
    else:
        print("Invalid choice, please try again.")
# This code is a simple menu-driven program that allows the user to add new users, show all users, or exit the program. It also includes a function to show statistics about the users, such as the total number of users, average age, and most common university. The data is stored in a CSV file for easy manipulation and analysis.
# The program uses the csv module to read and write data in CSV format, making it easy to handle structured data. The menu function displays the available options, and the user can choose what action to perform. The program continues to run until the user chooses to exit.