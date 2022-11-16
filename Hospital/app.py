class Patients:
     def __init__(self,name,age,idd,bloodType) :
          self.__name = name
          self.__age = age
          self.__idd = idd
          self.__bloodType = bloodType
          #gets
     def getName (self):
          print("Name: 🎇 ")
          return self.__name
     def getAge (self):
          print("Age: 🎇 ")
          return self.__age
     def getId (self):
          print("Id : 🎇")
          return self.__idd
     def getBloodType (self):
          print("Blood type : 🎇")
          return self.__bloodType
          #sets
     def setName(self,name):
          self.__name = name
     def setAge(self,age):
          self.__age = age
          #deletes
     def delBloodType(self):
          del self.__bloodType

