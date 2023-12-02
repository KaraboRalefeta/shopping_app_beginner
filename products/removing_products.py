import json
def remove_pro(product_name):
    try:
        with open("products/products.json", "r") as f:
            products = json.load(f)
    except:
         products = {}
    if products.get(product_name) == None:
            return False
    else:
        del products[product_name]

    with open("products/products.json", "w") as jf:
        json.dump(products, jf, indent=4)
        return True