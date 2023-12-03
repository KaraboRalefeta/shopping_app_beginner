import json

def food_exists(food):
    try:
        with open("producs/producs.json", "r") as f:
            products = json.load(f)
            return products[food]
    except:
        return "Food doesn't exist quit yet."
    
def buying(user, food):
    with open("producs/producs.json", "r") as f:
        products = json.load(f)
    with open("user/user_info.json"):
        pass

    
    
   