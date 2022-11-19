import random
from GemasGame import Personaje

# self,nombre,fuerza,inteligencia,defensa,vida

B1 = Personaje("🐵 Lilu",20,1,5,10)
B2 = Personaje("🐜 Hormy",15,50,5,0)
V1 = Personaje("🦔 TopoTron",70,2,1,10)
V2 = Personaje("🤖 BobyTron",8,5,3,10)

print("Welcome a HormyGem 💎")
print(" 1 para 🐵  Lilu\n 2 para 🐜 Hormy \n 3 para 🦔 TopoTron\n 4 para 🤖 BobyTron")

def usuarioselect(usuarioselect):
    if usuarioselect == 1:
        usuarioselect = B1
    elif usuarioselect == 2:
        usuarioselect = B2
    elif usuarioselect == 3:
        usuarioselect = V1
    elif usuarioselect == 4:
        usuarioselect = V2
    return usuarioselect
usuario = usuarioselect(int(input("Escoge un personaje del 1 al 4: ")))

# Se asigna nuestro oponente
def maquinaselect(maquinaselect):
    if maquinaselect == 1:
        maquinaselect = B1
    elif maquinaselect == 2:
        maquinaselect = B2
    elif maquinaselect == 3:
        maquinaselect = V1
    elif maquinaselect == 0:
        maquinaselect = V2
    return maquinaselect

maquina = maquinaselect(random.randint(0,2))


# Guardamos el dato.


print("Tu personaje seleccionado es: ", usuario.nombre)
print("Tu contrincante en esta ronda es: ", maquina.nombre)

usuario.atributos()
maquina.atributos()

print("💥Inicializamos los personajes para la batalla💥")
print(usuario.atributos())
print(maquina.atributos())

def pelea(usuario,maquina):
    usuario.atacar(maquina)
    if maquina.validarVivo and usuario.validarVivo:
        maquina.atacar(usuario)
    else:
        True
while usuario.vida >= 1 and maquina.vida >= 1:
    pelea(usuario,maquina)
    break

usuario.atributos()
maquina.atributos()

if usuario.vida == 0:
    print ("Gano: ", {maquina.nombre})
elif maquina.vida == 0:
    print ("Gano: ", {usuario.nombre})
else:
    print("Empate")