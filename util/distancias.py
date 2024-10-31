import math

def haversine(lat_origem, long_origem, lat_destino, long_destino):
    lat_origem_rad = math.radians(lat_origem)
    long_origem_rad = math.radians(long_origem)
    lat_destino_rad = math.radians(lat_destino)
    long_destino_rad = math.radians(long_destino)

    # Raio da Terra em metros
    R = 6371000

    delta_lat = lat_destino_rad - lat_origem_rad
    delta_lon = long_destino_rad - long_origem_rad

    # Fórmula de Haversine
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_origem_rad) * math.cos(lat_destino_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distância em metros
    distance = R * c
    return distance