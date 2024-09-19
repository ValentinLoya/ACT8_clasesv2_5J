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
        frutas = ("Banana","Fresa","Mango")
        print("tuplas: ")
        print(frutas)
        for fru in frutas:
            print(fru)
        animales = {"Caballo","Gato","Perro"}
        print("conjunto: ")
        print(animales)
        for ani in animales:
            print(ani)
        dicc = {
        "Nombre": "Valentin",
        "Apellido": "Loya",
        "Edad": 17 }
        print("Diccionario: ")
        print(dicc)
        for x, y in dicc.items():
            print(x, y)
# creacion de objeto
info=Datos(1.81,84.5)

# utilizando el obj. --> info
info.mostrar_datos()
print("Lista de Autos Deportivos Valentin Foya")
info.mi_lista()
