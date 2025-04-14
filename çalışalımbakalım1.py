## 30 Günlük Python challenge
# 1. Gün: 14.04.2025
# Merhaba! Ben Aybars.
# Marmara Üniversitesi'nde okuyorum.
# Ekonomi ve Yönetim Bilişim Sistemleri çift anadal yapıyorum.
# Veri bilimiyle ilgileniyorum.
# Python öğreniyorum çünkü __________.
import os
isim = input("Adın ne?")
universite = input("Hangi üniversitede okuyorsun?")
bolum = input("Hangi bölümde okuyorsun?")
ilgi = input("Hangi alanda ilgin var?")
neden = input("Neden Python öğreniyorsun?")
dosya_yolu = r"C:/Users/aybar/OneDrive/Masaüstü/birincigün.txt"

with open(dosya_yolu, "a") as file:
    file.write("-----\n")
    file.write(f"Ad: {isim}\n")
    file.write(f"Universite: {universite}\n")
    file.write(f"Bolum: {bolum}\n")
    file.write(f"Ilgi Alani: {ilgi}\n")
    file.write(f"Neden Python Ogreniyorsun: {neden}\n")
    file.write("-----\n\n")
os.system("cls")
print("Bilgileriniz kaydedildi.")
