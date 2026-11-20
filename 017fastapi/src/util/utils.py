import json

filePath = "src/data/product.json"


def get_all_products():
    with open(filePath, "r") as file:
        return json.load(file)


def save_all_products(products):
    with open(filePath, "w") as file:
        json.dump(products, file, indent=4)