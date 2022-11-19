class Personaje():
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida) -> None:

        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.xp = 0
        self.aguante = fuerza * vida
        self.volar = False

    def atributos(self):
        print(self.nombre, sep=":")
        print("💫 Fuerza: ", self.fuerza)
        print("💫 Inteligencia: ", self.inteligencia)
        print("💫 Defensa: ", self.defensa)
        print("💫 Aguante: ", self.aguante)
        print("💫 Experiencia: ", self.xp)
        print(f"💫 ¿Puede volar?, {self.volar}")
        print("💫 Vida: ", self.vida)

    def subirNivel (self, fuerza, inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        self.xp = self.xp + 1

    def validarVivo(self):
        return self.vida > 0

    # Morir del personaje
    def __gameover(self):
        self.vida = 0
        print(f"El personaje {self.nombre} ha muerto.")
    # Hacer daño al enemigo
    def damage(self,enemigo):
        return self.fuerza - enemigo.defensa
    # Metodo atacar
    def atacar(self,enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, "ha realizado", damage, "puntos de daño a", enemigo.nombre)

        if enemigo.validarVivo():
            print("La vida de",{enemigo.nombre}, "es", {enemigo.vida})
        else:
            enemigo.__gameover()
            print(f"😣 GameOver {enemigo.nombre}")