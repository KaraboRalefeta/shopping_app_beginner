import json

def signup(name, password):
    encryption_num = len(name)*2

    password = [chr(ord(i) * encryption_num) for i in password]
    password = "".join(password)
    try:
        with open("user/userinfo.json", "r") as f:
            users = json.load(f)
    except:
        users = {}
    users[name] = {
        "password" : password,
        "amount": 3000,
        "admin": False
    }
    with open("user/userinfo.json", "w", encoding='utf-8') as uf:
        json.dump(users, uf, indent = 4)