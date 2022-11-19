class Caracther():
     def __init__(self, name, strength,inteligence,defense):
        self.name = name
        self.strength = strength
        self.inteligence = inteligence
        self.defense = defense
        self.live = 3
        self.experience = 0
        self.keep = strength * self.live
        self.fly = False

     def atributes (self):
        print("💫 name:", self.name)
        print("💫 name:", self.strength)
        print("💫 name:", self.inteligence)
        print("💫 name:", self.defense)
        print("💫 name:", self.live)
        print("💫 name:", self.experience)
        print("💫 name:", self.keep)
        print("💫 name:", self.fly)

     def levelUp(self,strength,inteligence,defense):
          self.strength = self.strength + strength
          self.inteligence = self.inteligence + inteligence
          self.defense = self.defense + defense

     def ifAlive(self):
          return self.live > 0

     def damage(self,nemesis):
          return  nemesis.defense -  self.strength   

     def __gameover(self):
          self.live = 0

     def attack(self,nemesis):
          damage = self.damage(nemesis)
          nemesis.live =  nemesis.live - damage 
          print(f"{self.name} has attacked {damage} {nemesis.name} ")
          if nemesis.ifAlive():
               print(f"Nemesis live{nemesis.name} is {nemesis.live} ")
          else:
               nemesis.__gameover()
               print("GAME OVER.")


