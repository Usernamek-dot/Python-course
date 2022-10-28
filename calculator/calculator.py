from add import *
from subtract import *
from divide import *
from multiply import *
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
      if select not in range(1,5): 
         print("🩸Only must contain 1  character to the corresponding options.")
         continue
      else:
            if select == 1:
               print("You are gonna add.  🔗 ")
               try :
                  num = int(input("Type a number:"))
                  num2 = int(input("Type a number:"))
                  add(num,num2)
               except ValueError :
                   print("🩸 Just a number.  Are you sure it`s a number ?")
                   continue

            elif select == 2:
               print("You are gonna subtract 📷📸 ")   
            elif select == 3:
               print("You are gonna multiply ⚔")   
            elif select == 4:
               print("You are gonna divide 📲 ")   
            break
dictionary = {
   '1': 'Add',
   '2': 'Subtract',
   '3': 'Multiply',
   '4': 'Divide'
}
print ("++++++++++ 🐍  CALCULATOR 🐍++++++++++")
showOptions(dictionary)
selectingOption()

