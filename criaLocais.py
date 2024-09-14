from distancias import haversine
from context import Locais
import pandas as pd

locaisClass = Locais()

destino_lat = -23.5503898
destino_long = -46.6330809

csv = pd.read_csv('./locais_sp.csv')

locaisArr = list(csv.itertuples(index=False, name=None))

for local in locaisArr:
    distancia_linha_reta = round(haversine(destino_lat, destino_long, local[1], local[2]), 2)
    locaisClass.insert(local[0], local[1], local[2], distancia_linha_reta)