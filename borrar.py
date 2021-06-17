# -----------------------------  CREAR  ---------------------------------------
def Vehiculo():
    vehiculo = dict()
    vehiculo["id"] = int(input("Introduce el ID: "))
    vehiculo["fabricante"] = input("Introduce el FABRICATE: ")
    vehiculo["modelo"] = input("Introduce el MODELO: ")
    vehiculo["precio"] = int(input("Introduce el PRECIO en (€): "))
    vehiculo["color"] = input("Introduce el COLOR: ")
    vehiculo["motor"] = str(input("Introduce la MOTOR: "))

    vehiculos.append(vehiculo)

    return vehiculos
    print("--------------------------------------------------------")
    print("VEHICULO SUBIDO AL SISTEMA: ")


# ------------------------------BUSCAR O CONSULTAR ----------------------------------------
def busca_producto(id_vehiculo):
    for vehiculo in vehiculos:
        if vehiculo.id == id_vehiculo:
            return vehiculo


# -------------------------- BORRAR UNO ----------------------------------------
def borrar_un_producto(id):
    lista = 0
    for vehiculo in vehiculos:
        if vehiculo.id == id:
            break
        lista += 1
    return lista



# -------------------------- BORRAR TODO ----------------------------------------
def borrar_producto():
    vehiculos.clear()
    print(vehiculos)


# -------------------------- EDITAR ----------------------------------------
def editar_producto():
    for vehiculo in vehiculos:
        vehiculo.id = int(input("Introduce el ID: "))
        vehiculo.fabricante = input("Introduce el FABRICATE: ")
        vehiculo.modelo = input("Introduce el MODELO: ")
        vehiculo.precio = int(input("Introduce el PRECIO en (€): "))
        vehiculo.color = input("Introduce el COLOR: ")
        vehiculo.motor = (input("Introduce la MOTOR: "))


        print("-----------------------------------------------------")
        print("SE HA MODIFICADO EL VEHICULO CORRECTAMENTE: ")
        print(vehiculo)
        break