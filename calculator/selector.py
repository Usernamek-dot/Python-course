from validateNumber import *
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
            if select == 1: #add
               print("You are gonna add.  🔗 ")
               validateNum(1)
               continue
            elif select == 2: #subtract
               print("You are gonna subtract 📷📸 ")   
               validateNum(2)
               continue
            elif select == 3: #multiply
               print("You are gonna multiply ⚔")   
               validateNum(3)
               continue
            elif select == 4: #divide
               print("You are gonna divide 📲 ")   
               validateNum(4)
               continue
            else:
               print("Wanna go out? 🧶 y/n")
               break