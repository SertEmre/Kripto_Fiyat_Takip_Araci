import requests
def kripto_fiyat_takibi(coin,para):
    url='https://api.coingecko.com/api/v3/simple/price'
    params = {
        "ids" : coin,
        "vs_currencies": para
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        veri = response.json()
        if coin in veri:
            fiyat = veri[coin][para]
            print(f"{coin.capitalize()} fiyatı: {fiyat} {para}")
        else:
            print(f"{coin} API de yer almıyor.Coinin isimini kontrol ediniz.")
    else:
        print("Fiyat alınamadı.")

coin = input("Coinin ismini giriniz: ").lower()
para = input("Para birimini giriniz: ").lower()

kripto_fiyat_takibi(coin, para)

