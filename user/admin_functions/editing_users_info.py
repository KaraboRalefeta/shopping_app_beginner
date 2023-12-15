from user.signup.validate_info import user_exit
from user.login.validate_admin import admin_valid
import json
def edite_user_info(admin_username, admin_password, user):

    if admin_valid(admin_username, admin_password):
        if user_exit(user):
            with open("user/userinfo.json", "r") as f:
                users = json.load(f)

            change = input(f"what would you like to change about user {user}: ")
            while users.get(change) == None or change == "admin":
                print(f"Unfortunately there is no info saved as {change} for user {user}")
                print("These are the things you can change about the user (password, amount)")
                change = input(f"what would you like to change about user {user}: ")

            change_to = input("what would you like to change {change} to: ")
            while change == "amount" and change_to.isdigit() == False:
                change_to = input("Plese enter a number: ")
                if change_to.isdigit():
                    change_to = int(change_to)
                    
            users[user][change] = change_to

            with open("users/usesinfo.json", "w") as uf:
                json.dump(users, uf, indent = 4)
                return True

    return False