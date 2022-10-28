divide = lambda  number,number2 :   number / number2   
multiply = lambda  number,number2 :   number * number2   
subtract = lambda  number,number2 :   number - number2   
add = lambda  number,number2 :   number + number2 
def showOptions(x):
           for keys, values in dictionary.items():
                    print(f"{keys}.   {values} ")
def selectingOption():
   while True:
      try:
            select =  int(input("🧩  To select an option, type the corresponding number : "))
      except ValueError:
         print("🩸Invalid data, try again.")   
         continue
      except len(select) == 1:
         print("🩸Only must contain 1 character.")
      else:
         print("Success  🎋")      
         break
dictionary = {
   '1': 'Add',
   '2': 'Subtract',
   '3': 'Multiply',
   '4': 'Divide'
}
print ("++++++++++ 🐍  CALCULATOR 🐍++++++++++")
print(showOptions(dictionary))
selectingOption()

   
   # option = int(input("🧩  To select an option, type the corresponding number : "))
   # if option.string:
   #    print(" 🩸 Incorrect option,  try again.")
   # elif option == : 
   #    print("El número es impar")

