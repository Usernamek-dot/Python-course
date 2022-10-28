import random
lessThanFifteen = []
moreThanFifty=[]
betweenFortyfiveAndFifty=[]

randomNum = random.randint(0,100)
for x in range(0,100):
     if randomNum < 15:
          lessThanFifteen.append(randomNum)
          print(f"💫 This number is less than 15 :  {lessThanFifteen}")
          break
     elif randomNum > 50:
          moreThanFifty.append(randomNum)
          print(f"💢 Number greater than 50:  {moreThanFifty} ")    
          break
     elif randomNum > 45 & randomNum < 50 :
          betweenFortyfiveAndFifty.append(randomNum)
          print(f" 🔆 Number is between 45 and 50:  {betweenFortyfiveAndFifty} ")    
          break
     else:
          print("🥖 This number doesnt match with any list ")     



# Desarrolle un código que haga un recorrido de 100 números enteros de forma aleatoria, y determine:

# Cuántos son menores que 15.
# Cuántos son mayores que 50.
# Y cuántos están comprendidos entre 45 y 50.