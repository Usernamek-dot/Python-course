def sumFunction(number,anotherNumber):
     sum = number + anotherNumber
     return sum
      
x = "y"    
while not x != "y":     
     number = int(input("Type a number:"))
     anotherNumber = int(input("Type another number:"))
     result= sumFunction(number , anotherNumber)
     print(f"This is the result {result} ")
     x = input("Wanna continue ? y/n ").lower()
