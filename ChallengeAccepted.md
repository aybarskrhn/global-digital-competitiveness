# thirtydaypythonchallenge
# 30 Day Python Challenge!! I began this to improve my python skills as a beginner..
# 1st Day 14.04.2025 - Let's learn to save the data to a local file. 
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
