import json
def adding_pro(product_name, cost, description):
    with open("products/products.json", "r") as f:
        try:
            products = json.load(f)
            if products.get(product_name) != None:
                return False
        except:
            products = {}
    with open("products/products.json", "w") as jf:
        products[product_name] = {"cost": cost, "Desctiption" : description}
        json.dump(products, jf, indent= 4)
        return True
