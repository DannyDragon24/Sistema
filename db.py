import sqlite3

class database:
      def __init__(self,db):
            self.conexion = sqlite3.connect(db)
            self.cur = self.conexion.cursor()
            self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS DATOS(ID INTEGER PRIMARY KEY AUTOINCREMENT
                            ,NOMBRE VARCHAR(50),
                            APELLIDO VARCHAR(50),
                            SALDO INT(20),
                            ÚLTIMO_MOV INT(20),
                            FECHA VARCHAR(10))
                                              """)
      def fetch(self):
            self.cur.execute("SELECT*FROM DATOS")
            rows = self.cur.fetchall()
            return rows
      def __del__(self):
            self.conexion.close()
