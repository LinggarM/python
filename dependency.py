class ShopService:
   def changeProductPrice(price, product):
       product.changePrice(price)
 
class Product:
   def __init__(self, id, name, price):
       self.id = id
       self.name = name
       self.price = price
   def changePrice(self, value):
       self.price = value

prod1 = Product(5, "Motor", 1000)

ShopService.changeProductPrice(3000, prod1)
print(prod1.price)