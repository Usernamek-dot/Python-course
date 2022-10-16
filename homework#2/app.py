product1 = str(input("Type your product name:  "))
price1 = int(input("Type your product price: "))
product2 = str(input("Type your second product name:  "))
price2 = int(input("Type your product price: "))
product3 = str(input("Type your third product name:  "))
price3 = int(input("Type your product price: "))
totalPrice = price1 + price2 + price3
iva =   totalPrice * 0.19
totaIva=  iva + totalPrice

print("------TAX------")
print (f"-1  {product1.capitalize()}: {price1}  ")
print (f"-2  {product2.capitalize()}: {price2}  ")
print (f"-3  {product3.capitalize()}: {price3}  ")
print(f"The total amount of the products is:  {totalPrice}")
print(f"The iva amount is: {iva} ")
print(f"The total amount to pay with iva included is: {totaIva} ")


#     Realice un código que capture por medio de consola 3 nombres de productos, y 3 precios.
#     Una vez capturada la información debe generar una factura que me muestre lo siguiente en la consola:
#     Muestre cada producto y precio
#     Muestre el valor de la sumatoria de todos los precios de los productos.
#     Muestre el precio del IVA que es del 19% del total.
#     Muestre el valor total sumando el IVA.
