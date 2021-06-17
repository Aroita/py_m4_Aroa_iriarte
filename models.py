# -----------------------------  CLASE VEHICULO- Constructor y Comportamiento  ---------------------------------
class Vehiculo:
    def __init__(self, id_coche, fabricante, modelo,  precio, color, motor ):
        self.id_coche = id_coche
        self.fabricante = fabricante
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.motor = motor

    def __str__(self):
        return f"Vehiculo(id_coche={self.id_coche}, " \
               f"fabricante= {self.fabricante}, " \
               f"modelo= {self.modelo}, " \
               f"precio= {self.precio} " \
               f"color= {self.color}, " \
               f"motor= {self.motor}, " \
               f") \n "

    def __repr__(self):
        return self.__str__()

class Motor:
    def __init__(self, id_motor, cv, combustible):
        self.id_motor = id_motor
        self.cv = cv
        self.combustible = combustible


    def __str__(self):
        return f"Motor(id_motor={self.id_motor}, " \
               f"cv= {self.cv}, " \
               f"= {self.cv}, " \
               f") \n "

    def __repr__(self):
        return self.__str__()
