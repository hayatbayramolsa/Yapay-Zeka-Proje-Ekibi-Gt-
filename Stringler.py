# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:54:58 2020

@author: Hp 840
"""

# Tek tırnak çift tırnak

'Enes\'in arabası var'

# İndeksleme

a = "Enes"
a[1]

# İndeksi doğrudan değiştiremezsin.
a[2] = "i" # hatalı
a = "Enis"

# Len fonksiyonu
a = "Enes Tuzlu"
len(a)

# Uygulama 1: Kullanıcı şifre oluştursun. Şifresi en az 6 karakter, en çok 12 karakter olsun.
# Bu şartları karşılamazsa hata ver.

x = input("Şifrenizi oluşturun")
if(len(x) < 6):
    print("6dan uzun olsun")
elif(len(x) > 12):
    print("12den kısa olsun")
else:
    print("Şifreniz başarıyla oluşturuldu.")
    


"*" * 10

# %% Stringler üzerinde işlemler

# baş harfi büyük yapma
a = "python"
a.capitalize()

b = "python yapay zeka eğitimi"
b.capitalize()

# Her kelimenin baş harfini büyük yapma
b.title()

# Uygulama 2: Bir lorem ipsum metni al, tüm kelimelerin baş harflerini büyük yap.

# hepsini büyüt
c = "python"
c.upper()

# hepsini küçült
d = "ENES"
d.lower()


# büyükleri küçük yap küçükleri büyük yap
e = "Yapay Zeka"
e.swapcase()

# %% Sorgulamalar

a = "python"
a.isupper()
a.islower()

b = "Yapay Zeka Eğitimi"
b.istitle()



# Uygulama 3: Kullanıcının ismini iste, baş harfleri büyük değilse hata ver.

d = " "
d.isspace()


# Uygulama 4: Son uygulamayı geliştir. Önce boş mu değil mi ona bak, sonra aynısı.

e = input("İsminizi girin")
if (len(e) == 0):
    print("Bişey gir")
elif (e.isspace()):
    print("Bişey gir dedik de boşluk mu gir dedik")
elif (e.istitle()):
    print("Başarılı")
else:
    print("Baş harflerin hata!")
    

# %% Replace olayları
    
a = "sen yazılımcı mı oldun sen?"
a.replace("s", "ç")

a.replace("s", "ç", 1)

a.replace("ı", "")

# Uygulama 5: I am a good programmer. I am very good at this job. bu cümleyi geçmiş zamana çevir

a = "I am a good programmer. I am very good at this job. "
a.replace(" am ", " was ")


# %% Başlangıç bitiş sorgulaması

a = "Gebze Teknik Üniversitesi"
a.startswith("G")
a.endswith("Üniversitesi")

# Uygulama 6: a ile başlayıp a ile biten bir kelime iste. İki şartı da sağlıyorsa
# tamam. Yoksa hata ver

x = input("a ile başlayıp a ile biten kelime yaz")
if(len(x) <= 1):
    print("Bişey gir. Ama uzun olsun.")
elif (x.startswith("a") and x.endswith("a")):
    print("Doğru")
else:
    print("Yanlış")
    
# %% Karakterleri sayma
    
a = "kartal kalkar dal sarkar dal sarkar kartal kalkar"
a.count("a")

# Uygulama 7: İsmini ve ardından parolasını iste. Eğer parolasının
# içerisinde ismi geçiyorsa hata ver. Geçmiyorsa tamam.

# %% Alfanümerik sorgulaması

a = "python"
a.isalpha()
b = "1992"
b.isdigit()

c = "Gyte1992dekuruldu"
c.isalnum()


# Uygulama 8: İlk yaptığımız uygulamayı geliştir.
# şifrenin içinde hem harf hem sayı olmalı.









