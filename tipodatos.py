print("Clases v2 Valentin Loya")
# zona de clase
class Datos:
    # el constructor
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"estatura : {self.estatura} mts, Peso {self.peso} kg")
    def mi_lista(self):
        autos = ["Charger","Camaro","Mustang"]
        print(autos)
        for aut in autos:
            print(aut)
    def mi_tupla(self):
        frutas = ("Banana","Fresa","Mango")
        print(frutas)
        for fru in frutas:
            print(fru)
    def mi_conjunto(self):
        animales = {"Caballo","Gato","Perro"}
        print(animales)
        for ani in animales:
            print(ani)
    def mi_diccionario(self):
        dicc = {
        "Nombre": "Valentin",
        "Apellido": "Loya",
        "Edad": 17 }
        print(dicc)
        for x, y in dicc.items():
            print(x, y)
# creacion de objeto
info=Datos(1.81,84.5)

# utilizando el obj. --> info
info.mostrar_datos()

print("Lista de Autos Deportivos Valentin Foya")
info.mi_lista()

print("tupla de Valentin Foya")
info.mi_tupla()

print("conjunto de Valentin Foya")
info.mi_conjunto()

print("Diccionario de Valentin Foya")
info.mi_diccionario()

