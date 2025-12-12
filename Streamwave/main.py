from functions import *

load_users()
current_user = None

while True:
    if current_user:
        user_menu(current_user)
    main_menu()
    choice = input("Choose 1, 2 or 3: ")
    if choice == "1":
        register_user()
    elif choice == "2":
        current_user = login_user()
    elif choice == "3":
        break


        