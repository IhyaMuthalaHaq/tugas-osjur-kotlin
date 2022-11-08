print("-- GAME TEBAK ANGKA --")
import random
angka = random.randint(0,100)
percobaan = 0
while percobaan >=0 :
    jawaban = int(input(f"Masukan angka 1-100 : "))
    if jawaban < angka:
        percobaan += 1
        print("Angka terlalu kecil")
    elif jawaban > angka:
        percobaan += 1
        print("Angka terlalu besar")
    elif jawaban == angka:
        percobaan +=1
        print(f"Tebakanmu benar setelah {percobaan} kali")
        break
    if percobaan == 10 :
        print("Anda kurang beruntung")
        break