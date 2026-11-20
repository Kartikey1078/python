from fastapi import APIRouter, HTTPException
from src.util.utils import get_all_products
from src.dtos.productSchema import CreateProduct
from src.util.utils import save_all_products

product_routes = APIRouter()


@product_routes.get("/")
def getAllProducts(id:int = None): ## this is query parameters 
    allProducts = get_all_products()

    if id is None:
        return allProducts
    
    for product in allProducts:
        if product["id"] == id:
            return product
        
    raise HTTPException(
        status_code=404,
        detail="Product ID not found"
    )
        
# @product_routes.get("/{id}") ## it is a path parameter is comes from the url and fast api it into your function
# def getID(id:int):
    print(id)
    allProducts = get_all_products()
    for product in allProducts:
        if product["id"] == id:
            return product
        
    raise HTTPException(
        status_code=404,
        detail="Product ID not found"
    )

@product_routes.post("/create")
def create_products(product: CreateProduct):

    allProducts = get_all_products()

    product_data = product.model_dump()

    next_id = max(
        (p["id"] for p in allProducts),
        default=0
    ) + 1

    product_data["id"] = next_id

    allProducts.append(product_data)

    save_all_products(allProducts)

    return {
        "message": "Product created successfully",
        "product": product_data
    }

@product_routes.put("/update/{id}")
def updateProduct(id: int, product: CreateProduct):
    all_products = get_all_products()

    for index, p in enumerate(all_products):

        if p["id"] == id:

            updated_product = product.model_dump()
            updated_product["id"] = id

            all_products[index] = updated_product

            save_all_products(all_products)

            return {
                "message": "Product updated successfully",
                "product": updated_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product ID not found"
    )


@product_routes.delete("/delete/{id}")
def deleteProduct(id: int):
    allProduct = getAllProducts()

    for product in allProduct:
        if product["id"] == id:
            allProduct.remove(product)
            save_all_products(allProduct)
            return {"message":"Product deleted"}
    
    return {"message":"Product not found"}
        
    
        