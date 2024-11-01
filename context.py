import subprocess
import pyodbc
import os
import platform
from dotenv import load_dotenv

def install_odbc_driver():
    system = platform.system()
    
    if system == "Linux":
        # Example for Ubuntu/Debian-based systems
        print("Checking and installing ODBC driver on Linux...")
        subprocess.run("sudo apt-get update", shell=True)
        subprocess.run("sudo apt-get install -y unixodbc-dev", shell=True)
        subprocess.run("sudo apt-get install -y msodbcsql17", shell=True)


# Carregar variáveis de ambiente
load_dotenv()

install_odbc_driver()

class Database:
    def __init__(self):
        if platform.system() == "Windows":
            driver = "SQL Server"
        else: 
            
            driver = "ODBC Driver 17 for SQL Server"  # Ou "ODBC Driver 18 for SQL Server" se este estiver instalado

        print("DB_SERVER:", os.getenv("DB_SERVER"))
        print("DB_NAME:", os.getenv("DB_NAME"))
        print("DB_USER:", os.getenv("DB_USER"))
        print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
        print("DRIVER:", driver)

        # Conectar ao banco de dados com o driver adequado
        self.conn = pyodbc.connect(
            f'DRIVER={{{driver}}};'
            f'SERVER={os.getenv("DB_SERVER")};'
            f'DATABASE={os.getenv("DB_NAME")};'
            f'UID={os.getenv("DB_USER")};'
            f'PWD={os.getenv("DB_PASSWORD")};'
            f'TIMEOUT=120'
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