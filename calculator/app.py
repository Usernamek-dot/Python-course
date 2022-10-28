from selector import *
def showOptions(x):
   for keys, values in dictionary.items():
      print(f"{keys}.   {values} ")
dictionary = {
   '1': 'Add',
   '2': 'Subtract',
   '3': 'Multiply',
   '4': 'Divide'
}
print ("++++++++++ 🐍  CALCULATOR 🐍++++++++++")
showOptions(dictionary)
selectingOption()

