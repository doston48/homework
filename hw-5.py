password = input("Enter password: ")

if password == "":
    print("Password cannot be empty")
else:
    confirm = input("Re-enter password: ")
    if confirm == "":
        print("Password cannot be empty")
    elif password != confirm:
        print("Passwords do not match. Please try again.")
    elif len(password) < 8:
        print("Password too short. Minimum 8 characters required.")
    else:
        print("Password set successfully!")