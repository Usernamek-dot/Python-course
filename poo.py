class employee:
     #constructor
     def __init__(self,name,age,year,profesion) :
          self.name = name
          self.age = age
          self.year = year
          self.profesion = profesion
          print("Worker created.")
     def describe(self):
          return f"The dude`s name is {self.name}, he is a {self.profesion}. " 

statutoryAuditor = employee("Pepe","34","3930","builder")
manager = employee("Fulano","49","3923","chef")
print(statutoryAuditor.describe())