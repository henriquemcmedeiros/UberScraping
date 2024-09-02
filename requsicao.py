import requests
import time
from datetime import datetime
import pandas as pd

url = 'https://m.uber.com/go/graphql'

# CSRF Token -> Entra nos cookies e procura por "sid=" o valor até o ";"

headers = {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': 'marketing_vistor_id=d7cf0894-87ea-4cda-96c6-f161cbbdc10b; segmentCookie=b; utag_main_segment=a; utag_geo_code=BR; utag_main_optimizely_segment=b; udi-id=zfrHoRkp8EAOIKQuxdKLqnSfnb/FRAplzcBZZROMLgI/cPtXaefoAB7yfppRBSt8FaZS6OFVfmU2x4w0AkfCAq/D51hcZxIvUX6I8T1CEIWt49Fq3o0rCOq9gMDnz8zlGJrIt4dmtTxM37MszgxZpqgp1u5Krm3CVWIdL4wR+JPJciomv37GR0x2FlX8L606ePbiLtOSsCiZNNXt0JZn8g==ODmdB5E2jaIFSyY4sH5//Q==DoY3NTJpwp7U8LkVZdEQP2jstlNYWZeWMtBIlW6nDj8=; _cc=; _cid_cc=; _tt_enable_cookie=1; _ttp=IYkbYCaGkREXUnWnH3r4m8axRPL; _hjSessionUser_960703=eyJpZCI6ImFjNzk0ZDllLTg1YzAtNTQxMy05YWU0LTVhZTc0MDhkNDAxYiIsImNyZWF0ZWQiOjE3MjM2NDEzMzk2NTYsImV4aXN0aW5nIjp0cnVlfQ==; optimizelyEndUserId=oeu1723745463343r0.22427418846599045; ad_id=651862278850; _gcl_gs=2.1.k1$i1723750723; _gcl_dc=GCL.1723750772.Cj0KCQjwzva1BhD3ARIsADQuPnWIIj5NjJ4xAUI3YtiFYW_VC2Zi3E5xJJIkgNGIPSCIWWXu5HXwz9EaAiLuEALw_wcB; _gac_UA-7157694-35=1.1723750818.Cj0KCQjwzva1BhD3ARIsADQuPnWIIj5NjJ4xAUI3YtiFYW_VC2Zi3E5xJJIkgNGIPSCIWWXu5HXwz9EaAiLuEALw_wcB; _gcl_aw=GCL.1723750819.Cj0KCQjwzva1BhD3ARIsADQuPnWIIj5NjJ4xAUI3YtiFYW_VC2Zi3E5xJJIkgNGIPSCIWWXu5HXwz9EaAiLuEALw_wcB; utag_main_utm_campaign=CM2253871-search-google-brand_25_-99_BR-National_r_web_acq_cpc_pt_T1_Generic_BM_uber_kwd-12633382_651862278850_152896770931_b_c%3Bexp-1726170019072; utag_main_utmsource=AdWords_Brand%3Bexp-1726170019074; _clck=ntykgr%7C2%7Cfop%7C0%7C1687; sid=QA.CAESELpJBBshTkEcqUxCjH3tub4YoY7ctwYiATEqJGUxZTdlN2ViLWFjYzYtNDUzMy1hM2U1LTg0MDBjM2RiYjllYjJAXjYfhK1bffG9NOjuROZH5EbbppJl7SpslphR6NZ-UgbefwZyZ3XcRsJdqYDL-QD2uLaYgNHSX0qrcpnsM_6LNjoBMUIIdWJlci5jb20.0RXMu-8voTyz415KW4Tx6VvBwGezbd2Wz3CTqW6iGAw; csid=1.1727465249448.T+JifrMUTVoChTYrv7trpC1KFIVGUbgnSmEOEkncZrw=; _uetvid=9ea07cf05a3f11ef82236b48ae8961e4; udi-fingerprint=Xli6isUcoZ+1URF7hQ7OxBDwIW5q6OftRaTjqzsNbLYVbnZQYygj/Gr7QRtUTWSDkZhD0Ez1UNf4BGfPq4Up8w==NDm0uG7L2FZz4a6dzXuDWNxcNoe7CCTwc51vNixuiZY=; mp_adec770be288b16d9008c964acfba5c2_mixpanel=%7B%22distinct_id%22%3A%20%22e1e7e7eb-acc6-4533-a3e5-8400c3dbb9eb%22%2C%22%24device_id%22%3A%20%221915103e768458-0dccb4907135fd-26001e51-1fa400-1915103e769fd6%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%22e1e7e7eb-acc6-4533-a3e5-8400c3dbb9eb%22%2C%22utm_source%22%3A%20%22AdWords_Brand%22%2C%22utm_campaign%22%3A%20%22CM2253871-search-google-brand_25_-99_BR-National_r_web_acq_cpc_pt_T1_Generic_BM_uber_kwd-12633382_651862278850_152896770931_b_c%22%7D; _ga_DKGN4Z56QF=GS1.1.1725277834.8.0.1725277840.0.0.0; x-uber-analytics-session-id=c41f70e0-8574-454d-aad3-8be996f91ff0; utag_main__sn=7; utag_main_ses_id=1725277843412%3Bexp-session; utag_main__ss=0%3Bexp-session; _hjSession_960703=eyJpZCI6IjA3ZmZhYzJjLTU0NWMtNDZjOS05YjY1LTM5MTg2YTY3MGM5MyIsImMiOjE3MjUyNzc4NDQ0MjgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gid=GA1.2.591123929.1725277844; __cf_bm=pT8POkmRyVrvoXaEIGRZnbI5.Elttn0H8AyiVYeqiNs-1725277993-1.0.1.1-o9bOFm4dJctYbE54f1Qbb6rzF_RT7XMifUBf6RZABVbeW5633sIxXvhiWxsnAHo.fwyhnRy7Rzli.C0KAsWHnA; _ga=GA1.1.2049931067.1723641096; UBER_CONSENTMGR=1725277859657|consent:true; CONSENTMGR=1725277859658:undefined%7Cconsent:true%7Cc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1725277859659; _gat_gtag_UA_7157694_35=1; _ua_ph_id="4d054cea-416c-454b-8437-97e9e98b55cb"; km_ni=&mn9ujt1g=v4rwLwS3BrLyF4; OptanonConsent=isIABGlobal=false&datestamp=Mon+Sep+02+2024+22%3A21%3A59+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=202209.1.0&hosts=&consentId=9b47ff48-f5b3-4aa7-92c3-c44b99fae5b1&interactionCount=0&landingPath=https%3A%2F%2Fwww.uber.com%2Fbr%2Fpt-br%2Fbook%2F&groups=0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1&AwaitingReconsent=false; _gid=GA1.3.591123929.1725277844; __cf_bm=Na7si7YNcpxlD4HD2MLXy9LZAmFE7PsIb59ngIF5rEk-1725278025-0-AaaC49E2YaPZ8tRbBdmjRGgS+izhuYHKOTSkvKB7UyrDqlFS3sdykOW1Yd9W5obHcFnxb4UM0iBoJ1h5wuj6ALXBLXvLypPPkY3D5zLKZKKb+y7H5tMoXBONC6St6Zcx0A==; _fbp=fb.1.1723641096565.1278890708; csrf_token=QA.CAESELpJBBshTkEcqUxCjH3tub4YoY7ctwYiATEqJGUxZTdlN2ViLWFjYzYtNDUzMy1hM2U1LTg0MDBjM2RiYjllYjJAXjYfhK1bffG9NOjuROZH5EbbppJl7SpslphR6NZ-UgbefwZyZ3XcRsJdqYDL-QD2uLaYgNHSX0qrcpnsM_6LNjoBMUIIdWJlci5jb20.0RXMu-8voTyz415KW4Tx6VvBwGezbd2Wz3CTqW6iGAw; _clck=ntykgr|2|fop|0|1687',
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

# Iterando sobre as linhas do DataFrame
for index, row in df.iterrows():
    # Extraindo as coordenadas da origem
    origem_ponto = row['origem_ponto']
    origem_lat = row['origem_lat']
    origem_long = row['origem_long']
    
    # Extraindo as coordenadas do destino
    destino_ponto = row['destino_ponto']
    destino_lat = row['destino_lat']
    destino_long = row['destino_long']

    print(f"DE: {origem_ponto} PARA: {destino_ponto} INDEX: {index + 1}")

    data = {
        "operationName": "Products",
        "variables": {
            "includeRecommended": False,
            "destinations": [{"latitude": destino_lat, "longitude": destino_long}],
            "pickup": {"latitude": origem_lat, "longitude": origem_long}
        },
        "query": "query Products($destinations: [InputCoordinate!]!, $includeRecommended: Boolean = false, $pickup: InputCoordinate!, $pickupFormattedTime: String, $profileType: String, $profileUUID: String, $returnByFormattedTime: String, $stuntID: String, $targetProductType: EnumRVWebCommonTargetProductType) { products(destinations: $destinations, includeRecommended: $includeRecommended, pickup: $pickup, pickupFormattedTime: $pickupFormattedTime, profileType: $profileType, profileUUID: $profileUUID, returnByFormattedTime: $returnByFormattedTime, stuntID: $stuntID, targetProductType: $targetProductType) { ...ProductsFragment __typename }} fragment ProductsFragment on RVWebCommonProductsResponse { classificationFilters { ...ClassificationFiltersFragment __typename } defaultVVID hourlyTiersWithMinimumFare { ...HourlyTierFragment __typename } intercity { ...IntercityFragment __typename } links { iFrame text url __typename } productsUnavailableMessage renderRankingInformation tiers { ...TierFragment __typename } __typename } fragment BadgesFragment on RVWebCommonProductBadge { color text __typename } fragment ClassificationFiltersFragment on RVWebCommonClassificationFilters { filters { ...ClassificationFilterFragment __typename } hiddenVVIDs standardProductVVID __typename } fragment ClassificationFilterFragment on RVWebCommonClassificationFilter { currencyCode displayText fareDifference icon vvid __typename } fragment HourlyTierFragment on RVWebCommonHourlyTier { description distance fare fareAmountE5 farePerHour minutes packageVariantUUID preAdjustmentValue __typename } fragment IntercityFragment on RVWebCommonIntercityInfo { oneWayIntercityConfig(destinations: $destinations, pickup: $pickup) { ...IntercityConfigFragment __typename } roundTripIntercityConfig(destinations: $destinations, pickup: $pickup) { ...IntercityConfigFragment __typename } __typename } fragment IntercityConfigFragment on RVWebCommonIntercityConfig { description onDemandAllowed reservePickup { ...IntercityTimePickerFragment __typename } returnBy { ...IntercityTimePickerFragment __typename } __typename } fragment IntercityTimePickerFragment on RVWebCommonIntercityTimePicker { bookingRange { maximum minimum __typename } header { subTitle title __typename } __typename } fragment TierFragment on RVWebCommonProductTier { products { ...ProductFragment __typename } title __typename } fragment ProductFragment on RVWebCommonProduct { badges { ...BadgesFragment __typename } capacity cityID currencyCode description detailedDescription discountPrimary displayName estimatedTripTime etaStringShort fare fareAmountE5 fares { capacity discountPrimary fare fareAmountE5 hasPromo hasRidePass meta preAdjustmentValue __typename } hasPromo hasRidePass hourly { tiers { ...HourlyTierFragment __typename } overageRates { ...HourlyOverageRatesFragment __typename } __typename } iconType id is3p isAvailable legalConsent { ...ProductLegalConsentFragment __typename } meta parentProductUuid preAdjustmentValue productImageUrl productUuid reserveEnabled __typename } fragment ProductLegalConsentFragment on RVWebCommonProductLegalConsent { header image { url width __typename } description enabled ctaUrl ctaDisplayString buttonLabel showOnce __typename } fragment HourlyOverageRatesFragment on RVWebCommonHourlyOverageRates { perDistanceUnit perTemporalUnit __typename }"
    }

    response = requests.post(url, headers=headers, json=data)

    response_data = response.json()

    #print(response_data)
    tempo_chamada = datetime.now().strftime('%d/%m/%Y %H:%M')

    try:
        for products in response_data["data"]["products"]["tiers"]:
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
        time.sleep(10)


# Salva a resposta em um arquivo JSON
# with open('response_data.json', 'w') as file:
#     json.dump(response_data, file, indent=4, ensure_ascii=False)

# print("Dados salvos em 'response_data.json'.")
