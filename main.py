from services import auth_service



def welcome_message():
    print(f"Welcome to you Task-Management App")


# If user chose Login → call login function

# If user chose Register → call register function

# If user chose Exit → stop program
def main():
    welcome_message()
    while True:
        print(f"1. Login")
        print(f"2. Register")
        print(f"3. Exit")

        choice = input(f"\nPlease choose an option:").strip()

        if choice == 1:
            auth_service.login()
        
        elif choice == 2:
            auth_service.register()
        
        elif choice == 3:
            print(f"Goodbye!")
            break
        else:
            print(f"invalid option Try again!!")