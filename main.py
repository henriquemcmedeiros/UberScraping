import requests
import time
from datetime import datetime
import pandas as pd
import aiohttp
import asyncio

url = 'https://m.uber.com/go/graphql'

# CSRF Token -> Entra nos cookies e procura por "sid=" o valor até o ";"

headers = {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': 'u.bdid=2448a34b-b593-469c-a364-79d4167cd4c7; marketing_vistor_id=d7cf0894-87ea-4cda-96c6-f161cbbdc10b; segmentCookie=b; utag_main_segment=a; utag_geo_code=BR; utag_main_optimizely_segment=b; udi-id=zfrHoRkp8EAOIKQuxdKLqnSfnb/FRAplzcBZZROMLgI/cPtXaefoAB7yfppRBSt8FaZS6OFVfmU2x4w0AkfCAq/D51hcZxIvUX6I8T1CEIWt49Fq3o0rCOq9gMDnz8zlGJrIt4dmtTxM37MszgxZpqgp1u5Krm3CVWIdL4wR+JPJciomv37GR0x2FlX8L606ePbiLtOSsCiZNNXt0JZn8g==ODmdB5E2jaIFSyY4sH5//Q==DoY3NTJpwp7U8LkVZdEQP2jstlNYWZeWMtBIlW6nDj8=; _cc=; _cid_cc=; _tt_enable_cookie=1; _ttp=IYkbYCaGkREXUnWnH3r4m8axRPL; _hjSessionUser_960703=eyJpZCI6ImFjNzk0ZDllLTg1YzAtNTQxMy05YWU0LTVhZTc0MDhkNDAxYiIsImNyZWF0ZWQiOjE3MjM2NDEzMzk2NTYsImV4aXN0aW5nIjp0cnVlfQ==; optimizelyEndUserId=oeu1723745463343r0.22427418846599045; ad_id=651862278850; _gcl_gs=2.1.k1$i1723750723; _gcl_dc=GCL.1723750772.Cj0KCQjwzva1BhD3ARIsADQuPnWIIj5NjJ4xAUI3YtiFYW_VC2Zi3E5xJJIkgNGIPSCIWWXu5HXwz9EaAiLuEALw_wcB; _gac_UA-7157694-35=1.1723750818.Cj0KCQjwzva1BhD3ARIsADQuPnWIIj5NjJ4xAUI3YtiFYW_VC2Zi3E5xJJIkgNGIPSCIWWXu5HXwz9EaAiLuEALw_wcB; _gcl_aw=GCL.1723750819.Cj0KCQjwzva1BhD3ARIsADQuPnWIIj5NjJ4xAUI3YtiFYW_VC2Zi3E5xJJIkgNGIPSCIWWXu5HXwz9EaAiLuEALw_wcB; utag_main_utm_campaign=CM2253871-search-google-brand_25_-99_BR-National_r_web_acq_cpc_pt_T1_Generic_BM_uber_kwd-12633382_651862278850_152896770931_b_c%3Bexp-1726170019072; utag_main_utmsource=AdWords_Brand%3Bexp-1726170019074; sid=QA.CAESELpJBBshTkEcqUxCjH3tub4YoY7ctwYiATEqJGUxZTdlN2ViLWFjYzYtNDUzMy1hM2U1LTg0MDBjM2RiYjllYjJAXjYfhK1bffG9NOjuROZH5EbbppJl7SpslphR6NZ-UgbefwZyZ3XcRsJdqYDL-QD2uLaYgNHSX0qrcpnsM_6LNjoBMUIIdWJlci5jb20.0RXMu-8voTyz415KW4Tx6VvBwGezbd2Wz3CTqW6iGAw; csid=1.1727465249448.T+JifrMUTVoChTYrv7trpC1KFIVGUbgnSmEOEkncZrw=; _gid=GA1.2.591123929.1725277844; _clck=ntykgr%7C2%7Cfou%7C0%7C1687; _ga_DKGN4Z56QF=GS1.1.1725303080.10.0.1725303080.0.0.0; __cf_bm=Righ6O3tZthB.AfHmRj5lXDprH7BKcQqzWAxnLRMJNo-1725303223-1.0.1.1-3nSdzJfAOi.Z4xwZV_CIg66gouiW8MW7WBoJWEntVNCpsEft9oKxkfWoBKgmJ6P3df5nu_lSoifRf5OPYCJ.PA; utag_main__sn=8; utag_main_ses_id=1725303086388%3Bexp-session; utag_main__ss=0%3Bexp-session; _hjSession_960703=eyJpZCI6ImFmY2FlMWQ4LWVmY2YtNDA5ZS04NDU3LWIxNjVlYmRkM2M4ZiIsImMiOjE3MjUzMDMwODcyNjUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ua={"session_id":"263ca1f8-675b-4fe0-ad58-42dfdc11981a","session_time_ms":1725303250101}; mp_adec770be288b16d9008c964acfba5c2_mixpanel=%7B%22distinct_id%22%3A%20%22e1e7e7eb-acc6-4533-a3e5-8400c3dbb9eb%22%2C%22%24device_id%22%3A%20%221915103e768458-0dccb4907135fd-26001e51-1fa400-1915103e769fd6%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%22e1e7e7eb-acc6-4533-a3e5-8400c3dbb9eb%22%2C%22utm_source%22%3A%20%22AdWords_Brand%22%2C%22utm_campaign%22%3A%20%22CM2253871-search-google-brand_25_-99_BR-National_r_web_acq_cpc_pt_T1_Generic_BM_uber_kwd-12633382_651862278850_152896770931_b_c%22%7D; _uetsid=5e2bb3c0692311efa5a599a5ba28aafb; _uetvid=9ea07cf05a3f11ef82236b48ae8961e4; udi-fingerprint=/F66Y2GDaywt9mdMvGpXo2U61otj6mVbwsRpsgJINQ59X3KYPKBZPIZO+FOx9xWv0/a42p+Bvjnwq6jGBSZJfg==5h8B9czZDLOG67i78RDvoO06ca+hoPqs7BRGoX2megw=; _clsk=s0rabq%7C1725303467077%7C9%7C0%7Cq.clarity.ms%2Fcollect; UBER_CONSENTMGR=1725303616049|consent:true; CONSENTMGR=1725303616049:undefined%7Cconsent:true%7Cc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1725303616050; _ga=GA1.2.2049931067.1723641096; _gat_gtag_UA_7157694_35=1; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlVzZXItQWdlbnQiOiIiLCJ4LXViZXItY2xpZW50LWlkIjoiIiwieC11YmVyLWRldmljZSI6IiIsIngtdWJlci1jbGllbnQtdXNlci1zZXNzaW9uLWlkIjoiIiwidGVuYW5jeSI6InViZXIvcHJvZHVjdGlvbiJ9LCJpYXQiOjE3MjUzMDM3NjMsImV4cCI6MTcyNTM5MDE2M30.UX38DzZcYMC47Wds3Sr12yo3vrK9JKFl2UikhkPRrXE; _ga_XTGQLY6KPT=GS1.1.1725303087.8.1.1725303626.0.0.0; utag_main__pn=8%3Bexp-session; utag_main__se=26%3Bexp-session; utag_main__st=1725305427501%3Bexp-session',
    'origin': 'https://www.uber.com',
    'pragma': 'no-cache',
    'referer': 'https://www.uber.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'x-csrf-token': 'QA.CAESELpJBBshTkEcqUxCjH3tub4YoY7ctwYiATEqJGUxZTdlN2ViLWFjYzYtNDUzMy1hM2U1LTg0MDBjM2RiYjllYjJAXjYfhK1bffG9NOjuROZH5EbbppJl7SpslphR6NZ-UgbefwZyZ3XcRsJdqYDL-QD2uLaYgNHSX0qrcpnsM_6LNjoBMUIIdWJlci5jb20.0RXMu-8voTyz415KW4Tx6VvBwGezbd2Wz3CTqW6iGAw'
}

df = pd.read_csv('cruzamentos.csv')

async def fetch_data(session, data):
    async with session.post(url, json=data, headers=headers) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for index, row in df.iterrows():
            origem_ponto = row['origem_ponto']
            origem_lat = row['origem_lat']
            origem_long = row['origem_long']
            
            destino_ponto = row['destino_ponto']
            destino_lat = row['destino_lat']
            destino_long = row['destino_long']

            print(f"DE: {origem_ponto} PARA: {destino_ponto} INDEX: {index + 1}")
            tempo_chamada = datetime.now().strftime('%d/%m/%Y %H:%M')

            data = {
                "operationName": "Products",
                "variables": {
                    "includeRecommended": False,
                    "destinations": [{"latitude": destino_lat, "longitude": destino_long}],
                    "pickup": {"latitude": origem_lat, "longitude": origem_long}
                },
                "query": "query Products($destinations: [InputCoordinate!]!, $includeRecommended: Boolean = false, $pickup: InputCoordinate!, $pickupFormattedTime: String, $profileType: String, $profileUUID: String, $returnByFormattedTime: String, $stuntID: String, $targetProductType: EnumRVWebCommonTargetProductType) { products(destinations: $destinations, includeRecommended: $includeRecommended, pickup: $pickup, pickupFormattedTime: $pickupFormattedTime, profileType: $profileType, profileUUID: $profileUUID, returnByFormattedTime: $returnByFormattedTime, stuntID: $stuntID, targetProductType: $targetProductType) { ...ProductsFragment __typename }} fragment ProductsFragment on RVWebCommonProductsResponse { classificationFilters { ...ClassificationFiltersFragment __typename } defaultVVID hourlyTiersWithMinimumFare { ...HourlyTierFragment __typename } intercity { ...IntercityFragment __typename } links { iFrame text url __typename } productsUnavailableMessage renderRankingInformation tiers { ...TierFragment __typename } __typename } fragment BadgesFragment on RVWebCommonProductBadge { color text __typename } fragment ClassificationFiltersFragment on RVWebCommonClassificationFilters { filters { ...ClassificationFilterFragment __typename } hiddenVVIDs standardProductVVID __typename } fragment ClassificationFilterFragment on RVWebCommonClassificationFilter { currencyCode displayText fareDifference icon vvid __typename } fragment HourlyTierFragment on RVWebCommonHourlyTier { description distance fare fareAmountE5 farePerHour minutes packageVariantUUID preAdjustmentValue __typename } fragment IntercityFragment on RVWebCommonIntercityInfo { oneWayIntercityConfig(destinations: $destinations, pickup: $pickup) { ...IntercityConfigFragment __typename } roundTripIntercityConfig(destinations: $destinations, pickup: $pickup) { ...IntercityConfigFragment __typename } __typename } fragment IntercityConfigFragment on RVWebCommonIntercityConfig { description onDemandAllowed reservePickup { ...IntercityTimePickerFragment __typename } returnBy { ...IntercityTimePickerFragment __typename } __typename } fragment IntercityTimePickerFragment on RVWebCommonIntercityTimePicker { bookingRange { maximum minimum __typename } header { subTitle title __typename } __typename } fragment TierFragment on RVWebCommonProductTier { products { ...ProductFragment __typename } title __typename } fragment ProductFragment on RVWebCommonProduct { badges { ...BadgesFragment __typename } capacity cityID currencyCode description detailedDescription discountPrimary displayName estimatedTripTime etaStringShort fare fareAmountE5 fares { capacity discountPrimary fare fareAmountE5 hasPromo hasRidePass meta preAdjustmentValue __typename } hasPromo hasRidePass hourly { tiers { ...HourlyTierFragment __typename } overageRates { ...HourlyOverageRatesFragment __typename } __typename } iconType id is3p isAvailable legalConsent { ...ProductLegalConsentFragment __typename } meta parentProductUuid preAdjustmentValue productImageUrl productUuid reserveEnabled __typename } fragment ProductLegalConsentFragment on RVWebCommonProductLegalConsent { header image { url width __typename } description enabled ctaUrl ctaDisplayString buttonLabel showOnce __typename } fragment HourlyOverageRatesFragment on RVWebCommonHourlyOverageRates { perDistanceUnit perTemporalUnit __typename }"
            }

            tasks.append(fetch_data(session, data))

            # Executa o lote a cada 10 requisições
            if len(tasks) == 10:
                results = await asyncio.gather(*tasks)
                # Processa os resultados aqui, por exemplo, armazenando em um DataFrame
                for result in results:
                    try:
                        for products in result["data"]["products"]["tiers"]:
                            for product in products["products"]:
                                obj_dados = {
                                    "tipo": product["description"],
                                    "preco": round(product["fareAmountE5"]/100_000, 2),
                                    "tempo_estimado_viagem_min": round(product["estimatedTripTime"]/60, 2),
                                    "tem_promocao": product["hasPromo"],
                                    "data_atual": tempo_chamada
                                }
                    except:
                        print("Não houve resposta")
                        print(result)
                
                # Limpa as tasks e espera 5 segundos
                tasks = []
                await asyncio.sleep(10)
        
        # Executa as tarefas restantes
        if tasks:
            results = await asyncio.gather(*tasks)
            # Processa os resultados das tarefas restantes
            for result in results:
                try:
                    for products in result["data"]["products"]["tiers"]:
                        for product in products["products"]:
                            obj_dados = {
                                "tipo": product["description"],
                                "preco": round(product["fareAmountE5"]/100_000, 2),
                                "tempo_estimado_viagem_min": round(product["estimatedTripTime"]/60, 2),
                                "tem_promocao": product["hasPromo"],
                                "data_atual": tempo_chamada
                            }
                except:
                    print("Não houve resposta")
                    #await asyncio.sleep(10)

# Executa a função principal
asyncio.run(main())