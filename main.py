import requests
import re
from datetime import datetime
from context import Locais, Dados
import schedule
import time

# Configuração da URL e Headers
URL = 'https://m.uber.com/go/graphql'
HEADERS = {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'cookie': 'marketing_vistor_id=fad64476-ceb2-489e-abb2-734d2fb20c87; _ga=GA1.1.1072754013.1730373380; udi-id=iuK+eKUXby7tdl7Ta73/vwNiXWxrg4AEEls6iPVL6fpFJSBzxID+2MBrTF8jN53/sJtj8ZKeHWbgGgRgwHfY8ZKjbnSEEpm/JTAxi6T99HVbot6xvW4+8l8NYkDrBX58TSNksVvcgiE/xP+02lLX4BKcOzow3wx6kPI6ksFbZVyMTK4LtHb3m1LV8x+T8dXRoeqwK9hyrpwp8SLqkbyykg==ytP82McNrzRpceCvVsnVnA==vPpAnXMz3tGRqJf0Ix69wwAIy88Ma4fzSQIPR2x0Yxk=; _hjSessionUser_960703=eyJpZCI6ImJkMDBjZWQ3LWQ2NTUtNWViZC05YzFmLWEwODg2N2ZkMTU5OSIsImNyZWF0ZWQiOjE3MzAzNzMzNzk2MjcsImV4aXN0aW5nIjp0cnVlfQ==; u-cookie-prefs=eyJ2ZXJzaW9uIjoxMDAsImRhdGUiOjE3MzEwNzQ0MzgxNzksImNvb2tpZUNhdGVnb3JpZXMiOlsiYWxsIl0sImltcGxpY2l0IjpmYWxzZX0%3D; UBER_CONSENTMGR=1731074438179|consent:true; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1731074438180%7Cconsent:true; __cf_bm=Oaw8JPY8CTJFcL2qbLl4L8zrtKnRB81QAgARiqh5e00-1731942500-1.0.1.1-1Lea0.5Qw1gEk3u3eDe92XKOrjzC0LwZPib_FIaY2sfdxnDI3Pd8dbUEJbg4sqkkmJgt4GRVwC2eP1r84jGukg; utag_main__sn=3; utag_main_ses_id=1731942371821%3Bexp-session; _hjSession_960703=eyJpZCI6ImE5NjQ5ZDdiLTA2MzItNDI0Zi04ZWJmLTQ5MGU2NmY5MTBmMCIsImMiOjE3MzE5NDIzNzIyODgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; utag_main__ss=0%3Bexp-session; x-uber-analytics-session-id=e28ad41e-1f72-486e-a46b-37f669f6577b; isWebLogin=true; sid=QA.CAESEIBxZVcPzE51hCGBpBZA7BsYgcuLuwYiATEqJDBkMDljOWYyLTUyZDUtNGM5Yy05MmMyLTUxODM1MjFiYWM3MjJAvZ-toRwbhoIbUDBJCXYDWvWk2eMhtCTU00xznVK_93OSM4LyW6fRQwz-E3GT69H7yRSdz0uJ6vG14a4ExKYAuDoBMUIIdWJlci5jb20.J5X1T0ZzXuq9p6OX_5dd8dBa24WjhHge2o8DzNwmsnw; csid=1.1734534530253.bZjxmxEkeOYA/Qhvw82ZiNHUPK+GKcDD7Fcd/7/28lg=; _ua={"session_id":"d37f0af7-1c60-4ecd-ab68-84b216a3ce83","session_time_ms":1731942530418}; city_id_cookie_key=458; utag_main__pn=2%3Bexp-session; utag_main__se=4%3Bexp-session; utag_main__st=1731944203474%3Bexp-session; _ga_XTGQLY6KPT=GS1.1.1731942372.3.1.1731942403.0.0.0; mp_adec770be288b16d9008c964acfba5c2_mixpanel=%7B%22distinct_id%22%3A%20%220d09c9f2-52d5-4c9c-92c2-5183521bac72%22%2C%22%24device_id%22%3A%20%221933fcfcde55eb-08fc93e48e0d73-26011951-1fa400-1933fcfcde61472%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fauth.uber.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22auth.uber.com%22%2C%22%24user_id%22%3A%20%220d09c9f2-52d5-4c9c-92c2-5183521bac72%22%7D; _cc=AU7m8Cu8DVmWByw3sE0cfLSv; _cid_cc=AU7m8Cu8DVmWByw3sE0cfLSv; _tt_enable_cookie=1; _ttp=BPoYGhGZKG0xASSvZ7TZWfPi0hp.tt.1; _uetsid=b9115480a5be11efb45c63b08029c8b2; _uetvid=9ea07cf05a3f11ef82236b48ae8961e4; _clck=1ow764j%7C2%7Cfqz%7C0%7C1773; udi-fingerprint=b/D02QdguZQl5ihgbRz7g4ZbbYtbuRvQrD3EaB6wjohWVyJ0RchcQiVnVi5nz57FzKfjB17ZYE6ygV1UBWniSw==3ARFJIkBzImEPDsBSVb2Rq1ItDQ68whS9/rn43Jxz/U=; _clsk=1s2qoih%7C1731942404668%7C1%7C0%7Cq.clarity.ms%2Fcollect; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MzE5NDI1NDAsImV4cCI6MTczMjAyODk0MH0.4UggpZple47aWKMLUHA7Ll4B1wHnLwEQOu4kvgt_37s',
    'origin': 'https://www.uber.com',
    'referer': 'https://www.uber.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-csrf-token': 'QA.CAESEIBxZVcPzE51hCGBpBZA7BsYgcuLuwYiATEqJDBkMDljOWYyLTUyZDUtNGM5Yy05MmMyLTUxODM1MjFiYWM3MjJAvZ-toRwbhoIbUDBJCXYDWvWk2eMhtCTU00xznVK_93OSM4LyW6fRQwz-E3GT69H7yRSdz0uJ6vG14a4ExKYAuDoBMUIIdWJlci5jb20.J5X1T0ZzXuq9p6OX_5dd8dBa24WjhHge2o8DzNwmsnw'
}

# Configuração do ponto de destino
DESTINO_LAT = -23.5503898
DESTINO_LONG = -46.6330809
PONTO_FINAL = "Praça da Sé"

def extrair_dados_meta(meta):
    """Extrai informações da string 'meta'."""
    estimated_solo_time_match = re.search(r'"estimatedSoloOnTripTime":(\d+)', meta)
    unmodified_distance_match = re.search(r'"unmodifiedDistance":(\d+)', meta)

    estimated_solo_on_trip_time = int(estimated_solo_time_match.group(1)) if estimated_solo_time_match else None
    unmodified_distance = float(unmodified_distance_match.group(1)) if unmodified_distance_match else None

    return estimated_solo_on_trip_time, unmodified_distance

def processar_resposta(response, row, tempo_chamada, dados_class):
    """Processa a resposta da API e insere no banco."""
    try:
        result = response.json()
        for tier in result["data"]["products"]["tiers"]:
            for product in tier["products"]:
                estimated_solo_on_trip_time, unmodified_distance = extrair_dados_meta(product["meta"])

                tipo = product["description"]
                preco = round(product["fareAmountE5"] / 100_000, 2)
                tempo_estimado_viagem_sec = int(product["estimatedTripTime"])
                tempo_estimado_espera_sec = (
                    tempo_estimado_viagem_sec - estimated_solo_on_trip_time if estimated_solo_on_trip_time else None
                )
                tem_promocao = int(product["hasPromo"])

                # Insere os dados no banco
                dados_class.insert(
                    int(row[0]),
                    tempo_chamada,
                    preco,
                    tempo_estimado_viagem_sec,
                    tempo_estimado_espera_sec,
                    tipo,
                    tem_promocao,
                    unmodified_distance
                )
    except Exception as e:
        print(f"Erro ao processar a resposta: {e}")

def main():
    locais_class = Locais()
    dados_class = Dados()
    locais_arr = locais_class.select()

    tempo_chamada = datetime.now()

    print("Iniciando coleta.")
    for row in locais_arr[1:]:
        ponto_atual = str(row[1])
        origem_lat = float(row[2])
        origem_long = float(row[3])

        # Dados da requisição
        data = {
            "operationName": "Products",
            "variables": {
                "includeRecommended": False,
                "destinations": [{"latitude": DESTINO_LAT, "longitude": DESTINO_LONG}],
                "pickup": {"latitude": origem_lat, "longitude": origem_long}
            },
            "query": "query Products($destinations: [InputCoordinate!]!, $includeRecommended: Boolean = false, $pickup: InputCoordinate!) { products(destinations: $destinations, includeRecommended: $includeRecommended, pickup: $pickup) { tiers { products { description fareAmountE5 estimatedTripTime hasPromo meta } } } }"
        }

        response = requests.post(URL, headers=HEADERS, json=data)
        if response.status_code != 200:
            print(f"Erro na requisição para {ponto_atual}: {response.status_code}")
            continue

        processar_resposta(response, row, tempo_chamada, dados_class)

    print(f"Coleta finalizada às {datetime.now().strftime('%H:%M:%S')}")

# Agendamento da execução
schedule.every().hour.at(":00").do(main)

if __name__ == "__main__":
    print("Iniciando script...")
    while True:
        schedule.run_pending()
        time.sleep(1)