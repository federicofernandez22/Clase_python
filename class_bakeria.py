

class Bar:
    tipo = "bar"
    horario = "dia"

    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono


    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono

bar1 = Bar("Bakeria", "Caniada 83", 4656565)
bar2 = Bar("Chino", "Arturo Bas 90", 4657788)
bar3 = Bar("Propiedad Privada", "Arturo Bas 150", 4652121)



class Mozos(Bar):
    def __init__(self, nombre, direccion, telefono, nombreMozo, dni):
        super().__init__(nombre, direccion, telefono)
        self.__nombreMozo = nombreMozo
        self.__dni = dni

    def get_nombreMozo(self):
        return self.__nombreMozo
    def get_dni(self):
        return self.__dni

mozo1 = Mozos("Bakeria", "CAniada 83", 4656565, "Brian", 30888888)
mozo2 = Mozos("Chino", "Arturo Bas 69", 4565656, "Mariano Moreno", 29999900)

print(mozo2.get_dni())
print(mozo1.get_nombreMozo())