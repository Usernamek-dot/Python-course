import random
secret = random.randint(0,100)
for shots in range(10):
     num = int(input("Insert number."))
     if num == secret:
          print("🥩 Yo got the number.")
          break
     elif num < secret:
          print("🥙 Number is smaller than secret number.")     
     else:
          print("🥖 The number is higher than secret number. ")     
     if shots == 9:
          print("🥨 Game over.")     
          break
     else:
          print(f"You have {9-shots} shots left")     




#game