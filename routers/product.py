from fastapi import APIRouter
from models.product import Product

router = APIRouter()


#lista de productos:
products = [
    {
        "id": 1,
        "name": "product 1",
        "price": 20,
        "stock": 10
    },
    
    {
        "id": 2,
        "name": "product 2",
        "price": 20,
        "stock": 10
    }
]



#cargo la nueva ruta "/ products", genero la funcion obtener productos y que llame a la lista "products"
@router.get("/products")
def get_products():
    return products

#filtrar, obtener solo un producto, no todos
@router.get("/products/{id}")   #la ruta necesita el parametro id por eso en llaves.
def get_product(id: int):       #el parametro id se le debe entregar a la funcion, y el tipo tb.
    return list(filter(lambda item: item['id'] == id, products))     #filtrado: (funcion que hara la busqueda,listado donde se aplicara), item es el i de iteracion de busqueda
                                        #se hace la busqueda en los ids que sea igual al id que se esta recibiendo en la url (==)
                                        #convertir a lista y retornar.
                                        

#ahora con parametros query(lo anterior fue con parametros ruta)
#products/?stock = 10   :estructura de un parametro query en html
@router.get('/products/')
def get_products_by_stock(stock: int, price:float):
    return list(filter(lambda item: item['stock'] == stock and item['price'] == price, products)) #con dos querys



#vamos a hacer uso de nuestro modelo creado (se debe importar antes), metodo para agregar datos
@router.post('/products')
def create_product(product: Product):       #producto sera de tipo Product, asi no creo cada parametro como antes,lo llamoa a todo
    products.append(product)        #le agregamos anuestro listado mas productos
    return products

#metodo para modificar datos
@router.put('/products/{id}')

def update_product(id: int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]['name'] = product.name
            products[index]['stock'] = product.stock
            products[index]['price'] = product.price
    return products
        
#metodo para borrar datos
@router.delete('/products/{id}')

def delete_product(id: int):
    for item in products:
        if item['id'] == id:
            products.remove(item)
    return products