from GemasGame import Personaje
# Init: (self,nombre,fuerza,inteligencia,defensa,vida,xp)

class Samurai (Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada) -> None:
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def selecarma(self):
        opcionarma = int(input("Selecciones arma: 1 para espada corta y 2 para espada larga: "))
        if opcionarma == 1:
            self.espada = 8
        elif opcionarma == 2:
            self.espada = 12
        else:
            print("Esta espada no esta en tu inventario.")
    def atributos(self):
        super().atributos()
        print ("💫 Espada: ", self.espada)

    def damage(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

class Bombardero (Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,torpedo) -> None:
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.torpedo = torpedo
    def atributos(self):
        super().atributos()
        print("💫 Torpedo:", self.torpedo)
    def damage(self, enemigo):
        return self.inteligencia * self.torpedo - enemigo.defensa_


