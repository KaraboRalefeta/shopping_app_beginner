def user_exit(username):
    username = username.lower()
    try:
        with open("user/userinfo.csv", "r") as uf:
            users = uf.read().split('\n')
            for i in users:
                user, password = i.split(",")
                if user.lower() == username:
                    return True
    finally:      
        return False
    