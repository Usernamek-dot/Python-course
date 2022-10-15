import random
random.randInt(5,15)
product ="Pizzas 🍕  "  #para emojis es windows + .
price = int(10)
iva = float (0.19) 
name=input("Your name: 😎 ")
address = input("Your address: 🏪 ")
howManyPizzas=int(input("How many pizzas do you want: 🍕 "))
totalWithIva= price * iva + price
totalOrder=(totalWithIva * howManyPizzas)
print(totalOrder)

print(f"{name},  Your order is $ {totalOrder}" ,  )

orderProcessed = input("You want to continue ? ¿Yes or No? :  ")
if orderProcessed.lower == "yes":  
 print("processed.")
elif orderProcessed.lower == "no":
 print("Order canceled.")
else :
 print("I do not understand. Game over.")

 ticket = f"Invoice #{random.randInt(5,15)} PizzasPython  You paid {howManyPizzas} {product} totaling {totalOrder} You will receive it in 30  minutes at {address} "

 if totalOrder >= 50 and orderProcessed == "yes":
     print(ticket)










# Cree un archivo Python: AndresLopezAra_Tarea2_Pizzas.py
# Realice un script que capture la información de un cliente de una pizzería:
# Establezca el nombre del producto = Pizza 🍕, el precio, y el valor del IVA (7%).
# Pregunte al usuario, el nombre, la dirección donde se va a entregar el pedido y cuántas pizzas desea ordenar.
# Calcule sin imprimir el valor del pedido + el iva y genere un valor total de la orden.
 
# Con este valor total de la orden genere una condición, donde le pregunte si desea continuar con la orden según el valor.
# Si la persona continúa con la orden procese la orden, si no continúa con la orden, cancele la orden e imprima en la consola como quedó la orden si aceptada o candelada.
# * Adicionalmente si la persona continúa con la orden,  genere un recibo (print), en este recibo. debe usted imprimir todo los valores importantes de la orden, incluido, nombre, número de pizzas ordenadas, valor total de la orden y dirección de entrega.