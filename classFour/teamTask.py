user = input("Type username:  ")
pasS = input("Type password:  ")
age = int(input("Type age:  "))
name = input("Type name:  ")


if user == "Marvel" and pasS == "C14789":
     print(age,name)
     if age >= 18:
          print(f"Welcome!{user} ")
     else:  
          print("Ugg , too young.")
else:
     print("Access denied.")


# Cree un código que capture el usuario y la contraseña por consola a través de la función input.

# Determine si el usuario es igual a "Marvel" y la contraseña es igual a "C14789"

# Si el usuario y la contraseña son correctos pregunte la edad y el nombre del usuario por consola.

# Luego determine si la edad es mayor o igual a 18 años, y si cumple con esta condición, muestre en pantalla un aviso en consola que despliegue el nombre con un mensaje de bienvenida.

# Si la edad es menor a 18 años despliegue un mensaje que diga "No tiene la edad suficiente para acceder."

# Si el usuario y la contraseña son incorrectos muestre un mensaje que diga: "Acceso inhabilitado"