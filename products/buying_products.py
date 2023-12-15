import json

def food_exists(food):
    try:
        with open("producs/producs.json", "r") as f:
            products = json.load(f)
            return products[food]
    except:
        return "Food doesn't exist quit yet."
    
def buying(user, food):
    try:
        
        with open("products/products.json", "r") as pf:
            products = json.load(pf)
        with open("user/userinfo.json") as uf:
            users = json.load(uf)

        price = products[food]['price']
        amount = users[user]["amount"]

        if price > amount:
            return False

        users[user]["amount"] =  users[user]["amount"] - int(price)

        with open("user/userinfo.json", "w") as uf:
            json.dump(users, uf, indent = 4)
        return True
    except:
        return False

    
