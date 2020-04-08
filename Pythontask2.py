import random
import string


def user_details():
    fullname = input("What is your fullname (British format)?").upper()
    details = fullname.split()
    email = input("What is your email address?").upper()
    details.append(email)
    return details


def user_password(details):
    random_characters = "".join(random.choice(string.ascii_uppercase) for i in range(5))
    password = details[1][0:2] + details[0][-2:] + random_characters
    return password


def another_user():
    print("You can decide to add a new user")
    comment = input("Would you like to input another user? Yes or no").lower()
    return comment


library = {}
user = 0
status = True

while status:
    details = user_details()
    password = user_password(details)
    print(f"Your generated password is {password}.")
    password_consent = input("Are you contented with your password? Reply with a yes or no.").lower()

    preferred_password_loop = True
    while preferred_password_loop:

        if password_consent == "yes":
            details.append(password)
            library[user] = details
            break

        else:
            password = input("please input your preferred password of not less than 7 characters").upper()
            minimum_length = True
            while minimum_length:

                if len(password) >= 7:
                    print("Your password is valid.")
                    details.append(password)
                    library[user] = details
                    minimum_length = False
                    preferred_password_loop = False

                else:
                    password = input("please input a password with seven or more characters").upper()

    decision = another_user()
    if decision == "yes":
        status = True
        user += 1
    else:
        status = False
        for information in library:
            print(library.get(information))