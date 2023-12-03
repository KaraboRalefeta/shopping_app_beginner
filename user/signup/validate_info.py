def user_exit(username):
    username = username.lower()
    try:
        with open("user/userinfo.csv", "r",  encoding='utf-8') as uf:
            users = uf.read().split('\n')
            for i in users:
                
                user_info= i.split(",")
                if len(user_info) == 3:
                    user, password, cash = user_info
                    if user.lower() == username:
                        return True
    except:      
        return False