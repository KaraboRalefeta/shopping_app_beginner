import json
def adding_pro(product_name, cost, description):
    try:
        with open("products/products.json", "r") as f:
                products = json.load(f)
                if products.get(product_name) != None:
                    return False
    except:
        products = {}
    with open("products/products.json", "w") as jf:
        products[product_name] = {"price": cost, "Desctiption" : description}
        json.dump(products, jf, indent= 4)
        return True
adding_pro("apple", 150, "A doctor a day keeps the apple away")