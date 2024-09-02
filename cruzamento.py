import pandas as pd

# Carregar o CSV com os dados de locais
df = pd.read_csv('locais_sp.csv')

# Criar um DataFrame vazio para armazenar os cruzamentos
cruzamentos = pd.DataFrame(columns=['origem_ponto', 'origem_lat', 'origem_long', 'destino_ponto', 'destino_lat', 'destino_long'])

# Iterar sobre cada linha do DataFrame
for i, origem_row in df.iterrows():
    for j, destino_row in df.iterrows():
        if i != j:  # Evitar o cruzamento de um local com ele mesmo
            cruzamentos = cruzamentos._append({
                'origem_ponto': origem_row['Local'],
                'origem_lat': origem_row['Latitude'],
                'origem_long': origem_row['Longitude'],
                'destino_ponto': destino_row['Local'],
                'destino_lat': destino_row['Latitude'],
                'destino_long': destino_row['Longitude']
            }, ignore_index=True)

# Salvar o DataFrame de cruzamentos em um novo CSV
cruzamentos.to_csv('cruzamentos.csv', index=False)