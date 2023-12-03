import json
def user_exit(username):
    username = username.lower()
    try:
        with open("user/userinfo.json", "r",  encoding='utf-8') as uf:
            users = json.load(uf)
        if users.get(username) != None:
            return True
        else:
            return True
            
    except:      
        return False