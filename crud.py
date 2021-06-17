"""
Funciones CRUD
"""

# 1 - Importar driver
import mysql.connector as con

# 2 - Crear conexión a base de datos

def init_schema_execute():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="app")
    cursor = database.cursor()
    file = open("schema.sql")
    sql_content = file.read()
    file.close()
    sql_content = sql_content.replace("\n", "").replace("\t", "")
    sql_sentences = sql_content.split(";")

    for sql in sql_sentences:
        if sql:
            cursor.execute(sql + ";")

    cursor.close()
    database.close()


def init_schema_execute_multi():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="app")
    cursor = database.cursor()
    file = open("schema.sql")
    sql_content = file.read()
    file.close()
    cursor.execute(sql_content, multi=True )
    cursor.close()
    database.close()


def load_data():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="909990", database="app")
    cursor = database.cursor()
    file = open("data.sql")
    sql_content = file.read()
    file.close()
    sql_content = sql_content.replace("\n", "").replace("\t", "")
    sql_sentences = sql_content.split(";")

    for sql in sql_sentences:
        if sql:
            cursor.execute(sql + ";")
            database.commit()
    cursor.close()
    database.close()

#######################################################################
