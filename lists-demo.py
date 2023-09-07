# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluştrunuz.
markalar = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2- Liste kaç elemanlıdır?
result = len(markalar)

# print(markalar)
# print(result)

# 3- Listenin ilk ve son elemananı nedir?

result1 = markalar[0]
result2 = markalar[3]

# print(result1)
# print(result2)

# 4- Mazda değerini Toyota ile değiştirin.
markalar[-1] = "Toyota"
result = markalar
print(result)

# 5- Mercedes listenin bir elemanı mıdır?
result = "Mercedes" in markalar
print(result)

# 6- Listenin -2 indeksindeki değer nedir?
result = markalar[-2]
print(result)

# 7- Listenin ilk 3 elemanını alın.
result = markalar[0:3]
print(result)

result = markalar[:3]
print(result)

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
markalar[-2:] = ["Toyota", "Renault"]
result = markalar
print(result)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = markalar + ["Audi", "Nissan"]
print(result)

# 10- Listenin son elemanını silin.
del markalar[-1]
result = markalar
print(result)

# 11- Liste elemanlarını tersten yazdırınız.
result = markalar[::-1]
print(result)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

print(studentA) 
print(studentB)
print(studentC)

# 13- Liste elemanlarını yazdırınız.
result = studentA[0]
result = studentB[1]
result = studentC[3][2]


print(result)
