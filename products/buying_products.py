import json

def food_exists(food):
    try:
        with open("producs/producs.json", "r") as f:
            products = json.load(f)
            if products.get(food)!= None:
                return products[food]
            else:
                return False
    except:
        return False
    
def buying(user, amount, food):
    pass