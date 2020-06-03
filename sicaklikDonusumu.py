# -*- coding: utf-8 -*-

#farenheit = (celcius * 1.8) + 32


def farenheitToCelcius():
    
    farenheit = float(input("Lütfen Farenheit Değerini Giriniz : "))
    
    celcius = (farenheit  - 32 ) / 1.8
    
    print("-" * 32)
    
    print("Girilen Farenheit Değerin Celcius Değere Dönüşmüş Hali = " + str(celcius))
    
    
def celciusToFarenheit():
    
    celcius = float(input("Lütfen Celcius Değerini Gİriniz : "))
    
    farenheit = (celcius *1.8) + 32
    
    print("-" * 32)
    
    print("Gİrilen Celcius Değerin Farenheit Değere Dönüşmüş Hali : " + str(farenheit))
    

    
    
devamMi = True


while devamMi == True:
    
    print("\n 1 - Farenheit To Celcius \n 2 - Celcius To Farenheit \n 0 - Çıkış Yap")

    secim = int(input("Lütfen Bir Seçim Yapınız : "))

    if secim == 1:
        
        farenheitToCelcius()

    elif secim == 2:
        
        celciusToFarenheit()
    
    elif secim == 0:
        
        devamMi = False
        
    else:
        
        print("Yanlış Seçim Yapıldı")
        
    