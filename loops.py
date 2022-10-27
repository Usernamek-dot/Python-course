list =[1,2,3,4,6]
for x in list:
     print(x)
for x in range(10,20):
     print(x)
for x in range(list[:3],len(list)):
     print(x)
for x in list[:3,6]:
     print(x)
     
# looping a list

groupData={"item","item2","item3"}
for data in groupData:
     if data == "item5":
          print(  f"We have this item  {data.upper()} " )
     else:
          print("Not found")     
     
#looping a conjunto
listData = ["listItem","listItem2","listItem3","listItem4",]
for data in listData:
     if data == "item5":
          print(  f"We have this item  {data.upper()} " )
     else:
          print("Not found")     

dictionary ={"item":"value","item2":"value2","item3":"value3","item4":"value4",}
for key,value in dictionary.items():
  print(key, " = " , value)
#looping a dictionary


text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. umsan felis est, ut semper lorem egestas sed"

counter = 0
for x in text :
     if x == "a":
          counter+=1
print(f"There are `a`  {counter} times ")          

#looping a text