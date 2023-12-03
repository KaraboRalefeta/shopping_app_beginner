from user.signup.validate_info import user_exit
from user.login.validate_admin import admin_valid
import json
def upgrade_user(admin, password, user):
    if admin_valid(admin, password):
        if user_exit(user):
            with open("user/userinfo.json", "r") as f:
                users = json.load(f)
            with open("users/usesinfo.json", "w") as uf:
                users[user]["admin"] = True
                json.dump(users, uf, indent = 4)
                return True
    return False