import json
def admin_valid(username, password):
    username = username.lower()
    try:
        with open("user/userinfo.json", "r", encoding='utf-8') as uf:
            users = json.load(uf)
            if users.get(username) != None:
                password_user = [chr((int(ord(i)/(len(username*2))))) for i in users[username]["password"]]
                password_user = "".join(password_user)

                if password == password_user:
                    if users[username]["admin"] == True:
                        return True
            return False
    except:      
        return False