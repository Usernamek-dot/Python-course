from add import *
def validateNum():
      try :
          num = int(input("Type a number:"))
          num2 = int(input("Type a number:"))
          add(num,num2)
      except ValueError :
           print("🩸 Just a number.  Are you sure it`s a number ?")
