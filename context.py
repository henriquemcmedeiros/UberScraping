import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

DB_SERVER= "thyagoquintas.com.br"
DB_NAME= "uber"
DB_USER= "uber"
DB_PASSWORD= "uber"

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'DATABASE={DB_NAME};'
            f'UID={DB_USER};'
            f'PWD={DB_PASSWORD};'
            f'TIMEOUT=120'  # Aumenta o tempo limite para 120 segundos
        )

        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

class Locais(Database):
    def insert(self, nome, latitude, longitude, dist_haversine):
        sql = '''
            INSERT INTO LOCAIS (nome, latitude, longitude, dist_haversine)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (nome, latitude, longitude, dist_haversine))
        self.commit()

    def select(self):
        sql = '''
            SELECT * FROM LOCAIS
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

class Dados(Database):
    def insert(self, id_local, dia_Hora, preco, tempo_de_viagem, tempo_de_espera, tipo, tem_promo, dist_real):
        sql = f'''
            INSERT INTO DADOS (id_local, dia_Hora, preco, tempo_de_viagem, tempo_de_espera, tipo, tem_promo, dist_real)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(sql, id_local, dia_Hora, preco, tempo_de_viagem, tempo_de_espera, tipo, tem_promo, dist_real)
        self.commit()

    def select(self):
        sql = '''
            SELECT * FROM DADOS
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
