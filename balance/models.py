import sqlite3


class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultaSQL(self, consulta):

        conexion = sqlite3.connect(self.ruta)

        cursor = conexion.cursor()

        cursor.execute(consulta)

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])

        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos

    def borrar(self, id):
        consulta = "DELETE FROM movimientos WHERE id=?"
        conexion = sqlite3.connect(self.ruta)
        cursos = conexion.cursor()
        resultado = False
        try:
            # DELETE FROM movimientos WHERE id=3
            cursos.execute(consulta, (id,))
            conexion.commit()  # ejecuta
            resultado = True
        except:
            conexion.rollback()  # para que de marcha atras, del borrado
        conexion.close()
        return resultado
