from product_model import Product

def create_product_service(data):
    product = Product(
        name=data.name,
        price=data.price,
        description=data.description
    )

    return product

#Implementar BD e criar Read e Delete

def update_product_service(product, data):
    if data.name is not None:
        product.name = data.name
    if data.price is not None:
        product.price = data.price
    if data.description is not None:
        product.description = data.description

    return product