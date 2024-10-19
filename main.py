import requests
import re
from datetime import datetime
from context import Locais, Dados

url = 'https://m.uber.com/go/graphql'

# CSRF Token -> Entra nos cookies e procura por "sid=" o valor até o ";"

headers = {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'cookie': 'marketing_vistor_id=a13c4b10-779c-4e1d-a908-67665ad74127; segmentCookie=a; utag_main_segment=b; utag_main_optimizely_segment=b; udi-id=f1HtfsPEwTCWv2v1U1R5MoR0NohiO1jBs+2j+jOWmp+0JrqOykYVN9qHlSz5lbHAmbrYHBbhu4Kf/GImuOokXTB8zV2MGzAsv1bwkuXQwr5ToHZ+kB3eGx5U3MNM8WEDYgbsmsJv3obFYoRGPbiekKbZ08Cr0xadhfSgqHlrVlNCJRbpetACZekvre76EdvjishH8+Uv1ZNsmrXQyQrPhQ==wZaKDPJlIFGRZGJULXcrMA==fxAsLLruFX3tGftAEMj6qtMcYW3IW79eUu+UWLhvbNY=; _cc=; _cid_cc=; UBER_CONSENTMGR=1726348301423|consent:true; CONSENTMGR=1726348301423:undefined%7Cconsent:true%7Cc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1726348301423; __cf_bm=BmH27zzrt8Kq122ewRKs4C63IHY7ASrHytnstE8puQs-1729348118-1.0.1.1-FoQQwgQSUNqM2H5WSD1vPbobSs3ZWlwbMgWzRdzV_uslPVgMxsO3pNZvO4o7DedPnSZQb0PSP_Op5EOFAkATKA; utag_main__sn=5; utag_main_ses_id=1729348119108%3Bexp-session; utag_main__ss=0%3Bexp-session; _ua={"session_id":"3501fc12-3ec0-471a-8e98-5709daca7482","session_time_ms":1729348148672}; x-uber-analytics-session-id=e0b963ce-7731-45eb-ad4d-5e63b860ee89; isWebLogin=true; sid=QA.CAESED4iR4KC8kv2vtnfQk-gkqcYu57tuQYiATEqJDBkMDljOWYyLTUyZDUtNGM5Yy05MmMyLTUxODM1MjFiYWM3MjJA8otPDM3LVBUEXaLmY58QUetLryl7YD_ZhNqRDg0pquMvSTwX15i01Q4EiTVSLFvd2wQ48OPPFzkZ-CrQvJ1kFzoBMUIIdWJlci5jb20.MwWHC2C71cDEEiOsDsCWd3w7ni0P2zDQt3O_vVp6e1s; csid=1.1731940155326.TNLpuk816cBng9EBdLwEa6dukKktd6DbME0JPfT9yV8=; city_id_cookie_key=458; utag_main__pn=2%3Bexp-session; utag_main__se=6%3Bexp-session; utag_main__st=1729349958041%3Bexp-session; mp_adec770be288b16d9008c964acfba5c2_mixpanel=%7B%22distinct_id%22%3A%20%220d09c9f2-52d5-4c9c-92c2-5183521bac72%22%2C%22%24device_id%22%3A%20%2219137197cb0682-006a57c7fc6f2a-9111b2f-1fa400-19137197cb11ca1%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fauth.uber.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22auth.uber.com%22%2C%22%24user_id%22%3A%20%220d09c9f2-52d5-4c9c-92c2-5183521bac72%22%7D; udi-fingerprint=1784acZ901UOECuGZPnwFeMzSuWyIug00mSZG1pYxKgefxdjmtLNcxqtyjfwWFg+wIDESjd7lDe30xBEj6BVjA==JqTuTsof/fHIEGtswpgeO1h6VahqlblKWfDnSfjmKAs=; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjkzNDgxNjksImV4cCI6MTcyOTQzNDU2OX0.crqm25UhIL5K9HQ_cexPI0-sVr4yB3moi4hAYS7vGcU',
    'origin': 'https://www.uber.com',
    'referer': 'https://www.uber.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-csrf-token': 'QA.CAESED4iR4KC8kv2vtnfQk-gkqcYu57tuQYiATEqJDBkMDljOWYyLTUyZDUtNGM5Yy05MmMyLTUxODM1MjFiYWM3MjJA8otPDM3LVBUEXaLmY58QUetLryl7YD_ZhNqRDg0pquMvSTwX15i01Q4EiTVSLFvd2wQ48OPPFzkZ-CrQvJ1kFzoBMUIIdWJlci5jb20.MwWHC2C71cDEEiOsDsCWd3w7ni0P2zDQt3O_vVp6e1s'
}

def main():
    locais_class = Locais()
    dados_class = Dados()
    locais_arr = locais_class.select()
    
    # Definição do ponto de destino
    ponto_final = "Praça da Sé"
    destino_lat = -23.5503898
    destino_long = -46.6330809
    tempo_chamada = datetime.now() #.strftime('%d/%m/%Y %H:%M')
    
    for index in range(1, len(locais_arr)):
        row = locais_arr[index]
        ponto_atual = str(row[1])
        origem_lat = float(row[2])
        origem_long = float(row[3])
        
        # Dados da requisição
        data = {
            "operationName": "Products",
            "variables": {
                "includeRecommended": False,
                "destinations": [{"latitude": destino_lat, "longitude": destino_long}],
                "pickup": {"latitude": origem_lat, "longitude": origem_long}
            },
            "query": "query Products($destinations: [InputCoordinate!]!, $includeRecommended: Boolean = false, $pickup: InputCoordinate!) { products(destinations: $destinations, includeRecommended: $includeRecommended, pickup: $pickup) { tiers { products { description fareAmountE5 estimatedTripTime hasPromo meta } } } }"
        }
        
        print(f"DE: {ponto_atual} PARA: {ponto_final} INDEX: {index}")
        print("===========================================================")

        response = requests.post(url, headers=headers, json=data)
    
        # Exibe o resultado da requisição
        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code}")
            continue
        result = response.json()

        try:
            for tier in result["data"]["products"]["tiers"]:
                for product in tier["products"]:

                    # Extração de dados do campo "meta" usando expressões regulares
                    estimated_solo_on_trip_time_match = re.search(r'"estimatedSoloOnTripTime":(\d+)', product["meta"])
                    unmodified_distance_match = re.search(r'"unmodifiedDistance":(\d+)', product["meta"])

                    # Verifica se a correspondência foi encontrada e extrai os valores
                    estimated_solo_on_trip_time = int(estimated_solo_on_trip_time_match.group(1)) if estimated_solo_on_trip_time_match else None
                    unmodified_distance = float(unmodified_distance_match.group(1)) if unmodified_distance_match else None

                    tipo = product["description"]
                    preco = round(product["fareAmountE5"] / 100_000, 2)
                    tempo_estimado_viagem_sec = int(product["estimatedTripTime"])
                    tempo_estimado_espera_sec = tempo_estimado_viagem_sec - estimated_solo_on_trip_time if estimated_solo_on_trip_time else None
                    tem_promocao = int(product["hasPromo"])

                    # Insere os dados na tabela
                    dados_class.insert(int(row[0]), tempo_chamada, preco, tempo_estimado_viagem_sec, tempo_estimado_espera_sec, tipo, tem_promocao, unmodified_distance)
        except Exception as e:
            print(f"Erro no processamento da resposta: {e}")

if __name__ == '__main__':
    main()
