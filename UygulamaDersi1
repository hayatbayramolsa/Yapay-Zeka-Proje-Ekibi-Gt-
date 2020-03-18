# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:02:27 2020

@author: Hp 840
"""

Uygulama1: 1 ile 50 arasındaki tüm çift sayıları bir listede topla.

# liste.append() listeye eleman ekleme

*** Basit düşün! ***

liste = []
for i in range(50):
    if(i % 2 == 0):
        liste.append(i)
        

Uygulama2: Haftanın günlerini sayı ve isim olarak tutan bir sözlük yazın.
Kullanıcı bir sayı girdiğinde hangi gün olduğunu yazdırsın.
Örnek: 2 -> Salı

gunlerSozluk = {1 : "Pazartesi", 2: "Salı", 3 : "Çarşamba", 4 : "Perşembe", 5: "Cuma", 6: "Cumartesi", 7: "Pazar"}
sayi = input("Bir sayı gir")
print(gunlerSozluk[int(sayi)])


Uygulama3: Bir listenin içindeki sayılardan en büyüğünü döndüren fonksiyonu yazın. Integer değer verecek.

def enBuyuk(liste):
    enBuyukSayi = liste[0]
    
    for i in liste:
        if (i > enBuyukSayi):
            enBuyukSayi = i
            
    return enBuyukSayi


liste = [1, 9, 5, 15, 82, 2, 150, 19, 7]
enBuyuk(liste)


Uygulama4: Listedeki sayılardan en küçüğünü döndüren fonksiyonu yazın.


def enKucuk(liste):
    enKucukSayi = liste[0]
    
    for i in liste:
        if (i < enKucukSayi):
            enKucukSayi = i
    
    return enKucukSayi

liste = [-10, 9, 5, 15, 82, 2, 150, 19, 7]
enKucuk(liste)


Uygulama5: Bir listenin içinde kaç tane unique(benzersiz) değer olduğunu döndüren fonksiyonu yazın.
Unique: Sadece bir kez tekrarlanan değer.
İpucu: İç içe for döngüsü.


def kacUnique(liste):
    uniqueSayisi = 0
    
    for i in liste:
        say = 0
        for j in liste:
            if (i == j):
                say = say + 1
        if (say == 1):
            uniqueSayisi = uniqueSayisi + 1
            
    return uniqueSayisi

liste = [1, 9, 5, 15, 1, 2, 9, 4, 19, 15]
kacUnique(liste)


Uygulama6: Bir listede belirli bir elemanın kaç kez geçtiğini döndüren fonksiyonu yazın.
Fonksiyon liste ve eleman şeklinde 2 parametre almalı.

def kacKezGeciyor(liste, eleman):
    say = 0
    
    for i in liste:
        if (i == eleman):
            say = say + 1
    return say


liste = [1, 3, 5, 2, 4, 1, 1, 4]
kacKezGeciyor(liste, 4)

Genel kültür: Bir veri setinde verilerden birinin kaç kez yer aldığına sıklık(frequency) denir.


Uygulama 7: Bir listedeki en çok tekrar eden değeri döndüren fonksiyonu yazın.
İpucu: Bir önceki yazdığınız fonksiyondan faydalanın.

def tekrarlanan(liste):
    tekrarEtmeSayisi = 0
    
    for i in liste:
        sayi = kacKezGeciyor(liste, i)
        if (sayi > tekrarEtmeSayisi):
            tekrarEtmeSayisi = sayi
            enCokTekrarEden = i
    
    return enCokTekrarEden

liste = [1, 3, 5, 2, 4, 1, 1, 5, 3, 3, 3]
tekrarlanan(liste)

Genel kültür: Bir veri setinde sıklık(frequency) değeri en yüksek olana matematikte mod değeri, 
veri biliminde top veri denir.

Uygulama 8: Bir listenin medyan değerini veren fonksiyonu yaz. Veriler küçükten büyüğe sıralandığında
ortada kalan değerdir. Çift sayıda olursa ortadaki 2 değer.
liste.sort() Küçükten büyüğe sıralı hale getirir.

liste.sort()


1,2,3 -> Tek sayıdaysa direk ortadaki
1,2,3,4 -> Ortadaki 2 tane

1,2,3,4,5

def medyanBul(liste):
    liste.sort()
    
    # Eğer tek sayıysa
    if(len(liste) % 2 == 1):
        elemanSayisi = len(liste)
        ortaindex = int((elemanSayisi - 1) / 2)
        
        return liste[ortaindex]
    # Eğer çift sayıysa
    else:
        index = int(len(liste) / 2)
        return [liste[index - 1], liste[index]]
    
medyanBul([1,2,3,4,5,6,7,8])


Uygulama 9: Listedeki değerlerin aritmetik ortalamasını veren fonksiyonu yazın.


def ortalama(sayilar):
    a = 0
    b = len(sayilar)
    for i in sayilar:
        a = a + i
        
    return a / b

ortalama([3,4,5,6])


Uygulama 10: Verilen listeyi detaylıca analiz eden bir fonksiyon yaz.
Min değer, max değer, medyan, aritmetik ortalama, kaç tane unique değer var,
en çok tekrar eden hangisi ve bu kaç kez tekrar ediyor.

def analiz(liste):
    print("Minimum değer:")
    print(enKucuk(liste))
    print("Maximum değer:")
    print(enBuyuk(liste))
    print("Medyan:")
    print(medyanBul(liste))
    print("Aritmetik Ortalama:")
    print(ortalama(liste))
    print("Kaç unique değer var?")
    print(kacUnique(liste))
    print("Top value:")
    print(tekrarlanan(liste))
    print("Kaç kez tekrar ediyor")
    print(kacKezGeciyor(liste, tekrarlanan(liste)))


liste= [1,2,3,4,5,6,7]
analiz(liste)










