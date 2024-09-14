from distancias import haversine
from context import Locais, Deslocamentos

locaisClass = Locais()
deslocamentosClass = Deslocamentos()

locaisArr = locaisClass.select()

destino_lat = -23.5503898
destino_long = -46.6330809

for local in locaisArr:
    distancia_linha_reta = round(haversine(destino_lat, destino_long, local[2], local[3]), 2)
    deslocamentosClass.insert(local[0], distancia_linha_reta)