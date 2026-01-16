from services import auth_service

def welcome_message():
    print("\n" + "="*50)
    print("Welcome to Task-Management App")
    print("="*50)

def main_menu():
    # المنيو قبل ما يعمل login
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            auth_service.login()
            if auth_service.get_current_user():  # لو نجح الـ login
                dashboard_menu()
        elif choice == "2":
            auth_service.register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

def dashboard_menu():
    # المنيو بعد ما يعمل login
    while True:
        user = auth_service.get_current_user()
        print(f"\n--- Welcome {user.fname} ---")
        print("1. View Tasks")
        print("2. Create Task")
        print("3. Update Profile")
        print("4. Logout")
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            print("View Tasks (قريباً)")
        elif choice == "2":
            print("Create Task (قريباً)")
        elif choice == "3":
            auth_service.update_profile()
        elif choice == "4":
            auth_service.logout()
            break
        else:
            print("Invalid option!")

def main():
    welcome_message()
    main_menu()

if __name__ == "__main__":
    main()