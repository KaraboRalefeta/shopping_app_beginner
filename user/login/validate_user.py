def login(username, password):
    username = username.lower()
    try:
        with open("user/userinfo.csv", "r", encoding='utf-8') as uf:
            users = uf.read().split('\n')
            for i in users:
                user, password_user = i.split(",")
                if user.lower() == username:
                    password_user = [chr((int(ord(i)/(len(username*2))))) for i in password]
                    password_user = "".join(password)
                    if password == password_user:
                        return True
                    else:
                        return False
    finally:      
        return False