from os import system
print(" ")
print("Ruvalcaba Valverde Miguel Angel")
print("--------------------------------------")
print("--Tuples de Python--")
print("que es una Tuple: se utilisan para guardar varios items o objetos en una sola varaible, Tupla es uno de los cuatro tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos; los otros tres son Lista , Conjunto y Diccionario , todos con diferentes cualidades y usos.")
print("A difierencia de las listas los Tuples se abren con estos (), embes de corchetes [] y ademas es una colecion ordenada y inmutable")
print("Ejemplos")
union = ("undead","unluck","unfeel","unmove","unfair","untouchable","unstoppable","untruth","unavoidable","unchange","unjustice","unbreakable")
under = ("unseen","unfede","untell","unrepair","undecrease","untrust","unback","undraw","unburn","unchaste")
print(" ")
print("Miembros de Union")
print(union)
print("Este valor es de tipo:")
print(type(union))

print(" ")
print("Miembros de Under")
print(under)
print("Este valor es de tipo:")
print(type(under))
#esto fue una itrodusion basica de los tuples
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")

print("----------Tuple Length o Longitud de Tuple----------")
#esto cuenta cuantos items tiene un tuples 
print("El valor o cantidad de items que tiene el Under es:")
print(len(under))
print("El valor o cantidad de items que tiene el Union es:")
print(len(union))
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")

print("----------Crear una tupla con un elemento----------")
#Para que sea un Tuple tiene que tener una , sino sera un string
fruta = ("manzana",)
print(type(fruta))
#no es un tuple ya que le falta la , sino es un string
fruta = ("manzana")
print(type(fruta))
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")

print("----------Elementos de tupla: tipos de datos----------")
tuple1 = ("UmaSpring ", "UmaAutumn  ", "UmaWinter ", "UmaSummer ")
tuple2 = (777, 31, 7, 64, 80, 27)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
#Hay barios tipos de Tuple, con diferentes carapteres, str, int o bool
#pero tambien hay tuples mixtos
print("---")
deltarune = ("Kris", "Susie","Ralseit",31,2018,7.7,True)
print(deltarune)

KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
print("----------El constructor tuple()----------")
UN = tuple(("Unknown", "Unruin", "Unhealthy", "Unsleep"))
print(UN)
#Tambien puedes haser tuples de esta manera.
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
print("--------------------")
print("Rresultado: se aprendio de los tuples")
print(" ")
