import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Database:
    def __init__(self):
        # Conexão com o banco de dados usando pyodbc e variáveis do .env
        self.conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};'
            f'SERVER={os.getenv("DB_SERVER")};'
            f'DATABASE={os.getenv("DB_NAME")};'
            f'UID={os.getenv("DB_USER")};'
            f'PWD={os.getenv("DB_PASSWORD")}'
        )
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

class Deslocamentos(Database):
    def insert(self, id_local_origem, dist_haversine):
        sql = f'''
            INSERT INTO DESLOCAMENTOS (id_local_origem, dist_haversine)
            VALUES ({id_local_origem}, {dist_haversine})
        '''
        self.cursor.execute(sql, id_local_origem, dist_haversine)
        self.commit()

class Dados(Database):
    def insert(self, id_deslocamento, dia_Hora, preco, tempo_de_viagem, tempo_de_espera, tipo, tem_promo, dist_real):
        sql = f'''
            INSERT INTO DADOS (id_deslocamento, dia_Hora, preco, tempo_de_viagem, tempo_de_espera, tipo, tem_promo, dist_real)
            VALUES ({id_deslocamento}, {dia_Hora}, {preco}, {tempo_de_viagem}, {tempo_de_espera}, {tipo}, {tem_promo}, {dist_real})
        '''
        self.cursor.execute(sql, id_deslocamento, dia_Hora, preco, tempo_de_viagem, tempo_de_espera, tipo, tem_promo, dist_real)
        self.commit()
