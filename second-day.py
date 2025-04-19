import random
isimler = ["Ali", "Ayşe", "Mehmet", "Fatma", "Ahmet", "Zeynep", "Emre", "Elif", "Mustafa", "Aylin"]
bolumler = ["Bilgisayar Mühendisliği", "Elektrik Mühendisliği", "Makine Mühendisliği", "İnşaat Mühendisliği", "Endüstri Mühendisliği"]
sebepler = ["Python öğrenmek istiyorum çünkü kariyerime katkı sağlamak istiyorum.", "Python öğrenmek istiyorum çünkü veri analizi yapmak istiyorum.", "Python öğrenmek istiyorum çünkü yapay zeka projeleri geliştirmek istiyorum.", "Python öğrenmek istiyorum çünkü web geliştirme yapmak istiyorum.", "Python öğrenmek istiyorum çünkü oyun geliştirmek istiyorum."]
kayitlar = []
for i in range(3):
    print(f"\n{i+1}. Student")
    name = random.choice(isimler)
    degree = random.choice(bolumler)
    reason = random.choice(sebepler)
    kayitlar.append((name, degree, reason))

    print(kayitlar)

universities = ["Bologna", "Bocconi", "Marmara", "Istanbul", "Sabanci"]
universities.append("Stanford")
universities.remove("Istanbul")
for uni in universities:
    print(uni)

birth_date = input("Birth date (dd-mm-yyyy): ")

kisi = {
    "name": input("Name: "),
    "surname": input("Surname: "),
    "birth_date": birth_date,
    "university": input(f"Choose: {universities}: "),
}
if kisi["university"] not in universities:
    print("University not found")
else:
    print("University found")
    kisi["university"] = kisi["university"].capitalize()
if kisi["name"] == "":
    print("Name cannot be empty")
elif kisi["name"].isdigit():
    print("Name cannot be a number")
elif kisi["name"].isalpha() == False:
    print("Name cannot contain special characters")
if kisi["surname"] == "":
    print("Surname cannot be empty")
elif kisi["surname"].isdigit():
    print("Surname cannot be a number")
elif kisi["surname"].isalpha() == False:
    print("Surname cannot contain special characters")
if kisi["birth_date"] == "":
    print("Birth date cannot be empty")
print(kisi["name"], kisi["surname"], kisi["birth_date"], kisi["university"])


