import Motor
import Vehiculo
from crud import *
init_schema_execute()
motor = None




while True:
    print( """
    Menú de opciones: 
    1 - Consultar todos los Vehículos
    2 - Consultar un Vehículo y motor
    3 - Crear un nuevo Vehículo
    4 - Editar un Vehículo
    5 - Borrar un Vehículo
    6 - Borrar todos los Vehículos
    7 – Salir
    """)




    option = int(input("SELECCIONA UNA OPCION: "))
    print("--------------------------------------------------------")

    if option == 1:
        vehiculos = Vehiculo.find_all()
    print("Listado de vehiculo/ en base de datos:")
    print(vehiculos)

    elif option == 2:
    id_coche = int(input("Introduce el id de vehiculo:"))
    vehiculo = vehiculo.find_one(id_coche)
    if vehiculo is not None:
        print("El vehiculo solicitado es:")
    print(vehiculo)
    else:
    print("El vehiculo solicitado no existe")

    elif option == 3:
    vehiculo = Vehiculo.input_new()
    id_coche = Vehiculo.create(vehiculo)
    check = motor.create_motor(id_coche)
    if check:
        print("El vehiculo creado es correctamente")
    else:
        print("No se ha podido modificar el vehiculo")

    elif option == 4:
    print("Introduce el id del vehicle que quieres editar:")
    id_coche = int(input("Introduce un id:"))
    elif option == 5:
    id_coche = int(input("Introduce el id de vehiculo:"))
    check = vehiculo.delete_one(id_coche)
    if check:
        print("El vehiculo a sido borrado correctamente ")
    else:
        print("No se ha podido borrar el vehiculo")
    elif option == 6:
    print("Esto borrará todos los vehiculos de la base de datos.")
    confirm = bool(int(input("¿Está seguro de que quiere borrar todos? (1 Yes, 0 No)")))
    if not confirm:
        continue

    vehiculo.delete_all()
    print("Vehiculos borrados correctamente")
else:
    if option == 7:
        break




