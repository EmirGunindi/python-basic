website = "htpp://www.pythonders.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = " Hello World ".strip()
print(result)
# Eğer sadece soldan silmek istersek result = " Hello World ".lstrip()
# Eğer sadece sağdan silmek istersek result = " Hello World ".rstrip()


# 2- "www.google.com" içindeki google bilgisi haricindeki her karakteri silin.
result = "www.pythonders.com".strip("w.moc")
print(result)

# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın
result = course.lower()
print(result)

#Tüm karakterlerini büyük yapmak için result = course.upper()
#Sadece kelimelerin baş harfleri büyük olması için result = course.title()

# 4- "website" içinde kaç tana a karakteri vardır ?
result = website.count("a")
result = website.count("www")
result = website.count("www,0,10") #www karakteri 0.ncı index ile başlasın 10 a kadar gitsin.
print(result)


# 5- "website www" ile başlayıp com ile bitiyor mu ?
result = website.startswith("www")
print(result)

result = website.startswith("htpp")
print(result)

# Bitiş karakterlerini kontrol edelim.
result = website.endswith("com")
print(result)

# 6- "website" içinde ".com" ifadesi var mı ?
result = website.find("com")    #bulursa index sayısını gönderir.
result = website.find("com",0,10) #istenilen ifade 0 ile 10 index arasında var mı diye sorar.
result = course.find("Python")
print(result)

# 7- "course" içindeki karakterlerin hepsi alfabetik mi ?(isalpha, isdigit)
result = course.isalpha()
result = "Hello".isalpha()
result = course.isdigit()
result = "123".isdigit()
print(result)

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = "Contents".center(50, "*")
result = "Contents".ljust(50, "*")
result = "Contents".rjust(50, "*")
print(result)

# 9- "course" karakter dizisndeki tüm boşluk karakterlerini "-" ile değiştirirsin.
result = course.replace(" ", "-",)
result = course.replace(" ", "-",5)
result = course.replace(" ","")
print(result)

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.
result = "Hello World".replace("World","There")
print(result)
# 11- "course" karakter dizisinin boşluk karakterlerinden ayırın.
result = course.split(" ")
#result = result[2]
result = result[4]

print(result)
