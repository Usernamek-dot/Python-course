from add import *
from subtract import *
from divide import *
from multiply import *
def validateNum(x):
      try :
          num = int(input("Type a number:"))
          num2 = int(input("Type a number:"))
          if x == 1:
               add(num,num2)
          elif x == 2:
               subtract(num,num2)
      except ValueError :
           print("🩸 Just a number.  Are you sure it`s a number ?")
