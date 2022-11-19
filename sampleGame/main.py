from GemasGame import Personaje
from Guerreros import Samurai
from Guerreros import Bombardero
# Clase es la plantilla base esta contiene los atributos y los metodos.

# Propiedades - Atributos
# Estas propiedades me definen al objeto.

# Funciones - Metodos
# Las acciones que puede realizar el objeto.


# Instanciamos desde el metodo constructor __init__
# self,nombre,fuerza,inteligencia,defensa,vida

# Los buenos
# Pogy = Personaje("Pogy",10,1,5,100)
Hormy = Personaje("🐜 Hormy",10,1,5,100)
# Los Malos
Villanoide = Personaje("🦔 TopoTron",8,5,3,100)
Villanoide.volar = True

print("Inicializamos nuestros personajes")
print(Hormy.atributos())
print(Villanoide.atributos())

Hormy.fuerza = Hormy.fuerza + 2
print(f"La fuerza de {Hormy.nombre} es de: ",Hormy.fuerza)
print("🔎 Revisar atributos:")
Hormy.atributos()
print("⏫ Aqui subimos de nivel:")
Hormy.subirNivel(3,0,0)
Hormy.atributos()
print("👽 Quitar la vida por completo:")
# Hormy.__gameover()
print("Validamos si esta vivo:")
print(Hormy.validarVivo())
Hormy.atributos()

print("🐜😤 Antes del ataque")
Villanoide.atributos()
print(Hormy.damage(Villanoide))
print("⚔ Realizamos el ataque")
Hormy.atacar(Villanoide)
print("🐜🤕 Despues del ataque")
Villanoide.atributos()


print("🦔😤 Antes del ataque")
Hormy.atributos()
print(Hormy.damage(Villanoide))
print("⚔ Realizamos el ataque")
Villanoide.atacar(Hormy)
print("🦔🤕 Despues del ataque")
Hormy.atributos()



# Hormy.atributos()
# Villanoide.atacar(Hormy)

print("💥Inicializamos una nueva batalla💥")

goldenBor = Personaje("GolBor 🥞",30,48,30,100)
senShin = Samurai("SenShin 🤖",50,10,5,100,30)
TerriBol = Bombardero("Terribol 🦏",20,30,5,100,50)

print("Antes de atacar 🥳")
goldenBor.atributos()
senShin.atributos()
TerriBol.atributos()


goldenBor.atacar(TerriBol)
senShin.atacar(goldenBor)
TerriBol.atacar(senShin)

print("Despues de atacar 💥")
goldenBor.atributos()
senShin.atributos()
TerriBol.atributos()


# Bot contra  Bot

BitBee = Samurai("BitBee 🐝",20,10,4,1000,2)
RockerTu = Bombardero("RockerTu 🐲",5,15,4,1000,3)

def combate(player1,player2):
    ronda = 0
    while player1.validarVivo() and player2.validarVivo():
        print("Ronda: ", ronda)
        print("Accion de: ", player1.nombre)
        player1.atacar(player2)
        print("Accion de: ", player2.nombre)
        player2.atacar(player1)
        ronda = ronda + 1
    if player1.validarVivo():
        print("🏆 Ha ganado: ", player1.nombre)
    elif player2.validarVivo():
        print("🏆 Ha ganado: ", player2.nombre)
    else:
        "Hubo un empate 😅"

combate(BitBee,RockerTu)