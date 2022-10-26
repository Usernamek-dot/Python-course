
def listFunction(list):
     for value in list:
          print(f"This is my list {list} ")
def loopList(l):
     for x in l:
          print(f"value: {x}")
     l.sort()
     print(f"List in order: {l}  " )     

listItems = ["item","item2","item3"]
list =  ["item","item2","item3","item4"]   


listFunction(listItems)   
loopList(list)



