from products.product_operations import (
    add_products,
    update_products,
    read_products,
    delete_product
)




def main():

    while True:

        print("\n===== PRODUCT MANAGEMENT SYSTEM =====")

        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_products()
            break
        elif choice == "2":
            read_products()
            break
        elif choice == "3":
            update_products()
            break
        elif choice == "4":
            delete_product()
            break
        elif choice == "6":
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()
