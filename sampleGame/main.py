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
Hormy = Personaje("π Hormy",10,1,5,100)
# Los Malos
Villanoide = Personaje("π¦ TopoTron",8,5,3,100)
Villanoide.volar = True

print("Inicializamos nuestros personajes")
print(Hormy.atributos())
print(Villanoide.atributos())

Hormy.fuerza = Hormy.fuerza + 2
print(f"La fuerza de {Hormy.nombre} es de: ",Hormy.fuerza)
print("π Revisar atributos:")
Hormy.atributos()
print("β« Aqui subimos de nivel:")
Hormy.subirNivel(3,0,0)
Hormy.atributos()
print("π½ Quitar la vida por completo:")
# Hormy.__gameover()
print("Validamos si esta vivo:")
print(Hormy.validarVivo())
Hormy.atributos()

print("ππ€ Antes del ataque")
Villanoide.atributos()
print(Hormy.damage(Villanoide))
print("β Realizamos el ataque")
Hormy.atacar(Villanoide)
print("ππ€ Despues del ataque")
Villanoide.atributos()


print("π¦π€ Antes del ataque")
Hormy.atributos()
print(Hormy.damage(Villanoide))
print("β Realizamos el ataque")
Villanoide.atacar(Hormy)
print("π¦π€ Despues del ataque")
Hormy.atributos()



# Hormy.atributos()
# Villanoide.atacar(Hormy)

print("π₯Inicializamos una nueva batallaπ₯")

goldenBor = Personaje("GolBor π₯",30,48,30,100)
senShin = Samurai("SenShin π€",50,10,5,100,30)
TerriBol = Bombardero("Terribol π¦",20,30,5,100,50)

print("Antes de atacar π₯³")
goldenBor.atributos()
senShin.atributos()
TerriBol.atributos()


goldenBor.atacar(TerriBol)
senShin.atacar(goldenBor)
TerriBol.atacar(senShin)

print("Despues de atacar π₯")
goldenBor.atributos()
senShin.atributos()
TerriBol.atributos()


# Bot contra  Bot

BitBee = Samurai("BitBee π",20,10,4,1000,2)
RockerTu = Bombardero("RockerTu π²",5,15,4,1000,3)

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
        print("π Ha ganado: ", player1.nombre)
    elif player2.validarVivo():
        print("π Ha ganado: ", player2.nombre)
    else:
        "Hubo un empate π"

combate(BitBee,RockerTu)