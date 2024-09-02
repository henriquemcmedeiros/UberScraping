import requests

url = "https://m.uber.com/go/graphql"

headers = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-csrf-token": "1725277859658:undefined%7Cconsent:true%7Cc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1725277859659",
    "x-uber-rv-session-type": "desktop_session",
    "origin": "https://m.uber.com/",
    "referer": "https://m.uber.com/go/product-selection",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

data = {
    "operationName": "Products",
    "variables": {
        "includeRecommended": False,
        "destinations": [{"latitude": -23.5899618, "longitude": -46.6602269}],
        "pickup": {"latitude": -23.6697328, "longitude": -46.6995194}
    },
    "query": "query Products($destinations: [InputCoordinate!]!, $includeRecommended: Boolean = false, $pickup: InputCoordinate!, $pickupFormattedTime: String, $profileType: String, $profileUUID: String, $returnByFormattedTime: String, $stuntID: String, $targetProductType: EnumRVWebCommonTargetProductType) { products(destinations: $destinations, includeRecommended: $includeRecommended, pickup: $pickup, pickupFormattedTime: $pickupFormattedTime, profileType: $profileType, profileUUID: $profileUUID, returnByFormattedTime: $returnByFormattedTime, stuntID: $stuntID, targetProductType: $targetProductType) { ...ProductsFragment __typename }} fragment ProductsFragment on RVWebCommonProductsResponse { classificationFilters { ...ClassificationFiltersFragment __typename } defaultVVID hourlyTiersWithMinimumFare { ...HourlyTierFragment __typename } intercity { ...IntercityFragment __typename } links { iFrame text url __typename } productsUnavailableMessage renderRankingInformation tiers { ...TierFragment __typename } __typename } fragment BadgesFragment on RVWebCommonProductBadge { color text __typename } fragment ClassificationFiltersFragment on RVWebCommonClassificationFilters { filters { ...ClassificationFilterFragment __typename } hiddenVVIDs standardProductVVID __typename } fragment ClassificationFilterFragment on RVWebCommonClassificationFilter { currencyCode displayText fareDifference icon vvid __typename } fragment HourlyTierFragment on RVWebCommonHourlyTier { description distance fare fareAmountE5 farePerHour minutes packageVariantUUID preAdjustmentValue __typename } fragment IntercityFragment on RVWebCommonIntercityInfo { oneWayIntercityConfig(destinations: $destinations, pickup: $pickup) { ...IntercityConfigFragment __typename } roundTripIntercityConfig(destinations: $destinations, pickup: $pickup) { ...IntercityConfigFragment __typename } __typename } fragment IntercityConfigFragment on RVWebCommonIntercityConfig { description onDemandAllowed reservePickup { ...IntercityTimePickerFragment __typename } returnBy { ...IntercityTimePickerFragment __typename } __typename } fragment IntercityTimePickerFragment on RVWebCommonIntercityTimePicker { bookingRange { maximum minimum __typename } header { subTitle title __typename } __typename } fragment TierFragment on RVWebCommonProductTier { products { ...ProductFragment __typename } title __typename } fragment ProductFragment on RVWebCommonProduct { badges { ...BadgesFragment __typename } capacity cityID currencyCode description detailedDescription discountPrimary displayName estimatedTripTime etaStringShort fare fareAmountE5 fares { capacity discountPrimary fare fareAmountE5 hasPromo hasRidePass meta preAdjustmentValue __typename } hasPromo hasRidePass hourly { tiers { ...HourlyTierFragment __typename } overageRates { ...HourlyOverageRatesFragment __typename } __typename } iconType id is3p isAvailable legalConsent { ...ProductLegalConsentFragment __typename } meta parentProductUuid preAdjustmentValue productImageUrl productUuid reserveEnabled __typename } fragment ProductLegalConsentFragment on RVWebCommonProductLegalConsent { header image { url width __typename } description enabled ctaUrl ctaDisplayString buttonLabel showOnce __typename } fragment HourlyOverageRatesFragment on RVWebCommonHourlyOverageRates { perDistanceUnit perTemporalUnit __typename }"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
