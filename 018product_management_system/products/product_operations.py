
import json

FILE_PATH = "products/products.json"


# Read existing products
def load_products():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save products
def save_products(products):
    with open(FILE_PATH, "w") as file:
        json.dump(products, file, indent=4)


# ADD PRODUCT
def add_products():

    products = load_products()

    print("Add product")

    product_id = int(input("Enter product ID: "))

    for product in products:
        if product["id"] == product_id:
            print("Product ID already present")
            return

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    save_products(products)

    print("Product added successfully!")


# UPDATE PRODUCT
def update_products():

    products = load_products()

    product_id = int(input("Enter product ID: "))

    for product in products:

        if product["id"] == product_id:

            print("Product found!")
            print(product)

            product["name"] = input("Enter new name: ")
            product["price"] = float(input("Enter new price: "))
            product["quantity"] = int(input("Enter new quantity: "))

            save_products(products)

            print("Product updated successfully!")
            return

    print("Product ID not found")


# READ PRODUCT
def read_products():

    products = load_products()

    prod_id = int(input("Enter product ID: "))

    for product in products:

        if product["id"] == prod_id:
            print(product)
            return

    print("Product ID not found")


# DELETE PRODUCT
def delete_product():

    products = load_products()

    prod_id = int(input("Enter product ID: "))

    for product in products:

        if product["id"] == prod_id:

            products.remove(product)

            save_products(products)

            print("Product deleted successfully!")
            return

    print("Product ID not found")
