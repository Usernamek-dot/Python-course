divide = lambda  number,number2 :   number / number2   
multiply = lambda  number,number2 :   number * number2   
subtract = lambda  number,number2 :   number - number2   
add = lambda  number,number2 :   number + number2 
def loopSelect(i):
           for keys, value in dictionary.items():
                    print(keys,value)
def selecting():
          selection= input("  🧩  To select an option, type the corresponding number :")
          print(selection)

dictionary = {
   '1': 'Add',
   '2': 'Subtract',
   '3': 'Multiply',
   '4': 'Divide'
}
print ("++++++++++ 🐍  CALCULATOR 🐍++++++++++")
print(loopSelect(dictionary))
