from gems import Caracther
class Samurai (Caracther):    
     def __init__(self, name, strength, inteligence, defense,sword):
          super().__init__(name, strength, inteligence, defense,sword)
          self.sword = sword
     def damage(self,nemesis):
          return self.strength * self.sword - nemesis.defense