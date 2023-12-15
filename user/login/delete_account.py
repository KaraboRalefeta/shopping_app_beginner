import json
import user.login.validate_user as validate
def delete_user_function(username, password):
    try:
        with open("user/userinfo.json", mode = "r") as uf:
            users = json.load(uf)
    except:
        users = dict()
    user_credantials_correct = validate.login(username, password)
    if user_credantials_correct:
        del users[username]
        
    with open("user/userinfo.json", "w", encoding='utf-8') as uf:
        json.dump(users, uf, indent = 4)

    

    