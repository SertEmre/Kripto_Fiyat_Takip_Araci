import requests

geçmiş = []

def popüler_coinler_listesi():
    url = 'https://api.coingecko.com/api/v3/coins/markets' 
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page':1
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        tüm_coinler = response.json()
        popüler_coinler = [coin['id']for coin in tüm_coinler[:100]]
        print("\nEn popüler 100 coin:")
        for i, coin in enumerate(popüler_coinler, 1):
            print(f"{i}.{coin}")
        return popüler_coinler
    else:
        print("Popüler coin listesi alınamadı.")
        return

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
            if para in veri[coin]:
                fiyat = veri[coin][para]
                print(f"{coin.capitalize()} fiyatı: {fiyat} {para}")
                geçmiş.append({"coin":coin,"para":para,"fiyat":fiyat})
            else:
                print(f"{para()} API de yer almıyor.Geçerli bir para birimi giriniz.")
        else:
            print(f"{coin} API de yer almıyor.Coinin isimini kontrol ediniz.")
    else:
        print("Fiyat alınamadı.")

def geçmişi_göster():
    if geçmiş:
        print("\nGeçmiş fiyat sorguları:")
        for sorgu in geçmiş:
            print(f"{sorgu['coin']} {sorgu['para']}:{sorgu['fiyat']}")
    else:
        print("Geçmiş bulunamadı.")       

def ana_program():
    popüler_coinler = []
    while True:
        print("1-Popüler coinleri listele")
        print("2-Coin fiyatını sorgula")
        print("3-Geçmiş sorguları göster")
        print("4-Çıkış yap")

        seçim = input("Yapacağınız işlemi seçiniz:").strip()

        if seçim == '1':
            popüler_coinler = popüler_coinler_listesi()
        elif seçim == '2':
            coin = input("Coinin ismini giriniz: ").lower()
            para = input("Para birimini giriniz: ").lower()
            kripto_fiyat_takibi(coin, para)
        elif seçim == "3":
            geçmişi_göster()
        elif seçim == '4':
            print("Programdan çıkılıyor. Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")

ana_program()
