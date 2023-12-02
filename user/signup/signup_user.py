def signup(name, password):
    encryption_num = len(name)*2

    password = [chr(ord(i) * encryption_num) for i in password]
    password = "".join(password)
    
    with open("user/userinfo.csv", "a", encoding='utf-8') as uf:
        uf.write(f"{name},{password}\n")



        