sql_select_motor = """
SELECT v.id_coche, v.fabricante, v.modelo, v.color, v.precio, v.color, m.id_motor, m.cv,
        m.combustible
        FROM motor AS m INNER JOIN Vehiculo AS v ON m.id_coche = v.id_coche;
"""
sql_select_vehicle = "SELECT * FROM Vehiculo WHERE id_coche = %s;"

sql_insert_motor = """
INSERT INTO Motor ( cv, combustible, id_coche) 
VALUES (%s, %s, %s)
"""

sql_insert_vehicle = """
INSERT INTO Vehiculo (fabricante, modelo, precio, color)
VALUES (%s, %s, %s, %s)
"""

sql_exists_vehicle = """
SELECT 1 FROM Vehiculo
WHERE id_coche = %s;
"""

sql_update_vehicle = """
UPDATE Vehiculo
SET fabricante = %s, modelo = %s, previo = %s, color = %s
WHERE id_vehicle = %s;
"""

sql_delete_vehicle = """
DELETE FROM Vehiculo
WHERE id_coche = %s;
"""

sql_delete_vehicle = """
TRUNCATE TABLE Vehiculo;
"""