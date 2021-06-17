import mysql.connector as con
from sql import *
from models import Vehiculo, Motor



def find_all():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()

    cursor.execute(sql_select_motor)

    rows = cursor.fetchall()

    vehiculos = []
    for row in rows:
        if row[6] is not None:
            motor = Motor(row[6], row[7], row[8], row[9], row[10], row[11])
        else:
            motor = None
        vehiculo = Vehiculo(row[0], row[1], row[2], row[3], row[4], row[5], motor)
        vehiculos.append(vehiculo)

    cursor.close()
    database.close()
    return vehiculos

def find_one(id_coche):
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()

    params = (id_coche,)
    cursor.execute(sql_select_vehicle, params)

    row = cursor.fetchone()
    cursor.close()
    database.close()
    if row is None:
        return None

    if row[6] is not None:
        motor = Motor(row[6], None, None, None, None, None)
    else:
        motor = None
    vehiculo = Vehiculo(row[0], row[1], row[2], row[3], row[4], row[5], motor)

    return vehiculo


def input_new():
    print("A continuación introduzca los datos del nuevo vehiculo a crear:")
    fabricante = input("Introduce el fabricante: ")
    modelo = input("Introduce el modelo: ")
    precio = input("Introduce el precio: ")
    color = input("Introduce el color: ")


    has_motor = bool(int(input("¿El vehiculo tiene Motor? (0 - No, 1 - Sí)")))
    if has_motor:
        cv = int(input("Introduce cc: "))
        combustible = int(input("Combustible: "))
        id_motor =int(input("Introduce el id de vehiculo"))
        motor = Motor(id_motor, cv, combustible)
    else:
        motor = None

    return Vehiculo(None, fabricante, modelo, precio, color, motor)


def input_update():
    id_coche = int(input("A continuación introduzca el id del vehicle que desea editar:"))
    if not exists(id_coche):
        print("El vehicle solicitado no existe")
        return None

    fabricante = input("Introduce nombre del fabricante: ")
    modelo = input("Introduce nombre del modelo: ")
    precio = input("Introduce nombre del precio: ")
    color = input("Introduce el nombre del color: ")


    return Vehiculo(id_coche, fabricante, modelo, precio, color, None)


def exists(id_coche):
    if id_coche is None:
        return False

    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()

    param_id = (id_coche,)
    cursor.execute(sql_exists_vehicle, param_id)
    result = cursor.fetchone()

    cursor.close()
    database.close()

    return bool(result)


def create(vehiculo):
    if vehiculo is None:
        return False

    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()


    params = (
        vehiculo.fabricante,
        vehiculo.modelo,
        vehiculo.precio,
        vehiculo.color,

    )
    cursor.execute(sql_insert_vehicle, params)
    database.commit()

    cursor.close()
    database.close()
    return cursor.lastrowid


def update(vehiculo):
    if vehiculo is None:
        return False

    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()

    params = (
        vehiculo.fabricante,
        vehiculo.modelo,
        vehiculo.precio,
        vehiculo.color,
        vehiculo.id
    )
    cursor.execute(sql_update_vehicle, params)
    database.commit()
    result_num = cursor.rowcount
    cursor.close()
    database.close()
    return False if result_num == 0 else True


def delete_one(id_coche):
    if not exists(id_coche):
        print("El vehiculo solicitado no existe")
        return False

    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()

    params = (id_coche,)
    cursor.execute(sql_delete_vehicle, params)
    database.commit()
    result_num = cursor.rowcount
    cursor.close()
    database.close()
    return False if result_num == 0 else True


def delete_all():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="mysqlapp")
    cursor = database.cursor()
    cursor.execute(sql_delete_vehicle)
    cursor.close()
    database.close()