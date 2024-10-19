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
    'cookie': 'marketing_vistor_id=936e884c-8e65-4fe1-85d9-2bb4f995adfd; __cf_bm=ngNkr5.o56QiUKp04QWgAff5_Hj.p1N3y_6YXrY6.C8-1726348389-1.0.1.1-iPms1D4pR.M_AiEh6iKyzbW7OmSDu8tB.hkTrn_pRzOL59hFHP0.Eb_b6nSSK_htZJvJx2IOYQuy_ymUNuNs3Q; utag_main__sn=1; utag_main_ses_id=1726348261603%3Bexp-session; ad_id=; utag_main__ss=0%3Bexp-session; _hjSessionUser_960703=eyJpZCI6ImYzMzhlOTkxLTM0YWItNWU0Ny1iYzUwLTFhNGE2YmJjODBiZiIsImNyZWF0ZWQiOjE3MjYzNDgyNjE5NTAsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_960703=eyJpZCI6ImUyMzk4NWNlLTU5NTQtNDU0ZS1hY2IwLTA4YWY2YmI3ZjEzOSIsImMiOjE3MjYzNDgyNjE5NTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; UBER_CONSENTMGR=1726348262938|consent:true; CONSENTMGR=1726348262938:undefined%7Cconsent:true%7Cc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1726348262938; _gid=GA1.2.516159033.1726348263; _gcl_gs=2.1.k1$i1726348261; _clck=5qikiz%7C2%7Cfp6%7C0%7C1718; _gcl_dc=GCL.1726348294.CjwKCAjw6JS3BhBAEiwAO9waF5KzjFF3bY9n9WV8LGL650z2O5il_fIA90BAVnFDUT1DdjzHgAGl-xoCHJ4QAvD_BwE; x-uber-analytics-session-id=ffc1f32e-c4cf-4e4b-86fd-cc0c6e7ec283; udi-id=NaUrb7idJppcV+G9k2jauTD/Sw5kFPJOBUx2ObmcbkrxWqI/+fjOoZ4YqB2AKZRBK89airnwcCsWCJj5wAjHBkPTOzXKbpdiAtGBmbAf+wCSUQzt2OTvxgRGeSjAKUXKCNrEJN6gogcS9eWnS1ZNwtSg+YTahpfNx/Pz6i9Jb7G9MNnkHBx80K+9c/UWWfMeoEly+ESf+K6lIQHq+wVU6A==MvcOVqvnrKQZ4NYCxawZ0A==1W7CEXY1dw5JZJ+jVZMe3u+/16ECbj7mEpBkc4hCx+k=; isWebLogin=true; sid=QA.CAESEHAaUaxyB0aztAjKxSPNAzMYoJO2uAYiATEqJGUxZTdlN2ViLWFjYzYtNDUzMy1hM2U1LTg0MDBjM2RiYjllYjJAbhKa9aDJbRC6JA1Ui7jhdscj8w4y7AQ5L6DSezQEarhdo2WzsCS6BsdRUvW0p2NCyJIxJeZeRadihbDJwUNaAzoBMUIIdWJlci5jb20.luvf8pMq_RVuOizdYULmyhKKce4m205HoouYSTy5fnM; csid=1.1728940448375.AEa6856Q9GVKZEzpCU7MAEJ7Hna8gkuhT4SrXTuP3Ro=; _ua={"session_id":"76a1db34-7567-4844-b1bd-b8377055d797","session_time_ms":1726348448518}; utag_main__pn=2%3Bexp-session; _uetsid=d8c241e072dd11efba6b690c62c09a5d; _uetvid=d8c2723072dd11efbc94b90933611754; _fbp=fb.1.1726348321242.858086023778373445; _gcl_au=1.1.104584512.1726348321; utag_main__se=6%3Bexp-session; utag_main__st=1726350122223%3Bexp-session; utag_main_utm_campaign=CM2334257-googlepmax-googlepmax_25_-99_BR-National_r_web_acq_cpc_pt-BR_Generic______c%3Bexp-1728767522225; utag_main_utmsource=GooglePMAX%3Bexp-1728767522226; _tt_enable_cookie=1; _ttp=2rBGBU20va4ZR2V9QytilaFPbkq; _gcl_aw=GCL.1726348322.CjwKCAjw6JS3BhBAEiwAO9waF5KzjFF3bY9n9WV8LGL650z2O5il_fIA90BAVnFDUT1DdjzHgAGl-xoCHJ4QAvD_BwE; mp_adec770be288b16d9008c964acfba5c2_mixpanel=%7B%22distinct_id%22%3A%20%22e1e7e7eb-acc6-4533-a3e5-8400c3dbb9eb%22%2C%22%24device_id%22%3A%20%22191f260e69f137d-00d12cfeac06e3-26001151-1fa400-191f260e6a0152f%22%2C%22utm_source%22%3A%20%22GooglePMAX%22%2C%22utm_campaign%22%3A%20%22CM2334257-googlepmax-googlepmax_25_-99_BR-National_r_web_acq_cpc_pt-BR_Generic______c%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fauth.uber.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22auth.uber.com%22%2C%22%24user_id%22%3A%20%22e1e7e7eb-acc6-4533-a3e5-8400c3dbb9eb%22%7D; _ga_XTGQLY6KPT=GS1.1.1726348263.1.1.1726348322.0.0.0; _cc=; _cid_cc=; _ga=GA1.2.1779516301.1726348263; _gac_UA-7157694-35=1.1726348323.CjwKCAjw6JS3BhBAEiwAO9waF5KzjFF3bY9n9WV8LGL650z2O5il_fIA90BAVnFDUT1DdjzHgAGl-xoCHJ4QAvD_BwE; udi-fingerprint=Cr+r9RBnXdpCccbviRqd1//DFwG7cO8miHUgER/wIuyhYOTGzrZrMhLAG7Yqi81Ip5vT+k1HZz6jmHczr32t9Q==KZBy9l1VOnYX0X6892olqGIe9pXvPfTuWU2I/Yh+zC4=; _clsk=1wf3j4b%7C1726348324575%7C2%7C0%7Cq.clarity.ms%2Fcollect; _gat_gtag_UA_7157694_35=1; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjYzNDg0NzIsImV4cCI6MTcyNjQzNDg3Mn0.tJQklFt9mwpViOARNKiQb_av1Mm4oHTpN5y2xj4523w',
    'origin': 'https://www.uber.com',
    'referer': 'https://www.uber.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-csrf-token': 'QA.CAESEHAaUaxyB0aztAjKxSPNAzMYoJO2uAYiATEqJGUxZTdlN2ViLWFjYzYtNDUzMy1hM2U1LTg0MDBjM2RiYjllYjJAbhKa9aDJbRC6JA1Ui7jhdscj8w4y7AQ5L6DSezQEarhdo2WzsCS6BsdRUvW0p2NCyJIxJeZeRadihbDJwUNaAzoBMUIIdWJlci5jb20.luvf8pMq_RVuOizdYULmyhKKce4m205HoouYSTy5fnM'
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
