def add(number,number2):
     add = number + number2
     return add
def subtract(number,number2):
     subtract = number - number2
     return subtract
def multiply(number,number2):
     multiply = number * number2
     return multiply
divide = lambda  number,number2 :   number / number2   
# def divide(number,number2):
#      divide = number / number2
#      return divide
      
x = "y"    
while not x != "y":     
     number = int(input("Type a number:"))
     number2 = int(input("Type another number:"))
     result= add(number , number2)
     print(f"This is the result {result} ")
     x = input("Wanna continue ? y/n ").lower()

subtract(3,5)
multiply(2,55) 
divide(10,5)
