import pandas as pd
from geopy.geocoders import Nominatim

# Lista de locais
pontos = [
    "Centro Empresarial Vila Olímpia, São Paulo, SP, Brasil",
    "Shopping Campo Belo, São Paulo, SP, Brasil",
    "Vila Olímpia Corporate, São Paulo, SP, Brasil",
    "Shopping Jardins, São Paulo, SP, Brasil",
    "Avenida Brigadeiro Faria Lima, São Paulo, SP, Brasil",
    "Parque do Ibirapuera, São Paulo, SP, Brasil",
    "Shopping Interlagos, São Paulo, SP, Brasil",
    "Hospital das Clínicas, São Paulo, SP, Brasil",
    "Shopping Center Norte, São Paulo, SP, Brasil",
    "Parque da Juventude, São Paulo, SP, Brasil",
    "Mercado Municipal de São Paulo, São Paulo, SP, Brasil",
    "Shopping Metrô Tatuapé, São Paulo, SP, Brasil",
    "Parque do Carmo, São Paulo, SP, Brasil",
    "Hospital São Camilo, São Paulo, SP, Brasil",
    "Shopping Vila Maria, São Paulo, SP, Brasil",
    "Igreja Nossa Senhora do Brasil, São Paulo, SP, Brasil",
    "Parque da Água Branca, São Paulo, SP, Brasil",
    "Shopping Penha, São Paulo, SP, Brasil",
    "Museu do Futebol, São Paulo, SP, Brasil",
    "Instituto Butantan, São Paulo, SP, Brasil",
    "Parque Villa-Lobos, São Paulo, SP, Brasil",
    "Centro Cultural São Paulo, São Paulo, SP, Brasil",
    "Universidade de São Paulo (USP), São Paulo, SP, Brasil",
    "Igreja de São Bento, São Paulo, SP, Brasil",
    "Praça Roosevelt, São Paulo, SP, Brasil",
    "Rua Augusta, São Paulo, SP, Brasil",
    "Teatro Municipal de São Paulo, São Paulo, SP, Brasil",
    "Edifício Itália, São Paulo, SP, Brasil",
    "Biblioteca Mário de Andrade, São Paulo, SP, Brasil",
    "Templo Positivista, São Paulo, SP, Brasil",
    "Estação da Luz, São Paulo, SP, Brasil",
    "Museu de Arte de São Paulo (MASP), São Paulo, SP, Brasil",
    "Centro Cultural Banco do Brasil, São Paulo, SP, Brasil",
    "Parque da Independência, São Paulo, SP, Brasil",
    "Praça da Sé, São Paulo, SP, Brasil",
    "Conjunto Nacional, São Paulo, SP, Brasil",
    "Shopping Tatuapé, São Paulo, SP, Brasil",
    "Teatro J. Safra, São Paulo, SP, Brasil",
    "Parque Ecológico do Tietê, São Paulo, SP, Brasil",
    "Shopping Aricanduva, São Paulo, SP, Brasil",
    "Sesc Itaquera, São Paulo, SP, Brasil",
    "Parque do Carmo, São Paulo, SP, Brasil",
    "Shopping Metrô Itaquera, São Paulo, SP, Brasil",
    "Estádio do Corinthians, São Paulo, SP, Brasil",
    "Centro de Exposições Imigrantes, São Paulo, SP, Brasil",
    "Universidade Paulista (UNIP), São Paulo, SP, Brasil",
    "Avenida Paulista, São Paulo, SP, Brasil",
    "Edifício Copan, São Paulo, SP, Brasil",
    "Centro Cultural Banco do Brasil (CCBB), São Paulo, SP, Brasil",
    "Rua Vinte e Cinco de Março, São Paulo, SP, Brasil"
]

# Função para obter as coordenadas
def get_coordinates(location):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location)
    if location is None:
        return None, None
    return location.latitude, location.longitude

# Criar um DataFrame para armazenar os dados
data = {'Local': pontos}
df = pd.DataFrame(data)

# Check if all locations have coordinates
all_coordinates = df['Local'].apply(get_coordinates).tolist()
if len(set(all_coordinates)) != len(pontos):  # Check for duplicates (None)
    print("Warning: Missing coordinates for some locations!")

df[['Latitude', 'Longitude']] = df['Local'].apply(get_coordinates).tolist()  # Unpack directly

df.to_csv('locais_sp.csv', index=False)

print("Arquivo CSV criado com sucesso!")