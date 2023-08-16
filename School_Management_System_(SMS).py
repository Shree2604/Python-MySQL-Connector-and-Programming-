import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="6174",database="school_db")
cur_handler = conn.cursor()

def admin_menu():
    while True:
        print("")
        print("----------Welcome to Admin Menu Page---------")
        print("1. Register New Student")
        print("2. Register New Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")
        user_option = input("Select your option :")
        if user_option == "1":
            print("Register New Student")
        elif user_option == "2":
            print("Register New Teacher")
        elif user_option == "3":
            print("Delete Existing Student")
        elif user_option == "4":
            print("Delete Existing Teacher")
        elif user_option == "5":
            print("You are Logouted")
            break

def admin_login():
    print("")
    print("----------Welcome to Admin Login Page---------")
    print("")
    username = input("Enter username :")
    password = input("Enter password :")
    if username =='admin' and password =='admin':
       admin_menu()
    else:
        print("Wrong information for admin login!")

def main():
    while True:
        print("----------Welcome to School Management System---------")
        print("")
        print("1. Login option for Student")
        print("2. Login option for Teacher")
        print("3. Login option for Admin")

        user_option = input("Select your option :")
        if user_option == "1":
            print("Student Login")
        elif user_option == "2":
            print("Teacher login")
        elif user_option =="3":
            admin_login()
        else:
            print("Please check your option number & enter valid option!")

main()
