age = input("enter your age: ")

if not age.isdigit():
    print("invalid input")
else:
    age = int(age)
    if age <= 0:
        print("age canot be negative or zero")
    elif age >= 18:
        print("your allowed to vote")
    else:
        print("your to young")