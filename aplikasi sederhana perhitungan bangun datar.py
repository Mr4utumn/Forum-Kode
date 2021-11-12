#Project ke 2
#membuat konsep dasar rumus bangun datar
print(10*"="+"KONSEP BANGUN DATAR"+"="*10 + "\n")

pilihan = input(""" Pilih salah satu bangun datar yang ingin dicari:
a. Persegi
b. Persegi Panjang
C. Segitiga
D. Lingkaran
E. Trapesium
F. Jajargenjang
G. Layang-Layang
H. Belah Ketupat

Jawaban Anda: """)

if pilihan == "persegi" or pilihan == "Persegi" or  pilihan == "PERSEGI" or  pilihan == "a" or  pilihan == "A":
    #PERSEGI
    print(3*"="+" 1 - PERSEGI "+"="*3)

    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)

    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+" a. Luas")
        sisi = float(input("masukan panjang (cm): "))
        luas = sisi * sisi
        print("luas persegi adalah: ", luas)

    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+" b. Keliling")
        sisi = float(input("masukan panjang (cm): "))
        keliling = 4 * sisi
        print("keliling persegi adalah: ", keliling)


elif pilihan == "persegi panjang" or pilihan == "Persegi Panjang" or  pilihan == "PERSEGI PANJANG" or  pilihan == "b" or  pilihan == "B":
    #PERSEGI PANJANG
    print(3*"="+" 1 - PERSEGI PANJANG "+"="*3)

    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)
    ## Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        panjang = float(input("masukan panjang (cm): "))
        lebar = float(input("masukan lebar (cm): "))
        luas = panjang * lebar
        print("luas persegi panjang adalah: ", luas)

    ## Keliling
    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+"b. Keliling")
        panjang = float(input("masukan panjang (cm): "))
        lebar = float(input("masukan lebar (cm): "))
        keliling = 2 * (panjang + lebar) 
        print("keliling persegi panjang adalah: ", keliling)

elif pilihan == "segitiga" or pilihan == "Segitiga" or pilihan == "c" or pilihan == "C":
    #SEGITIGA
    print( 3*"="+" 3 - SEGITIGA "+"="*3)
    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)
    
    #Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        alas = float(input("masukan panjang alas: "))
        tinggi = float(input("masukan panjang tinggi: "))
        luas = 1/2 * alas * tinggi
        print("luas segitiga Anda adalah: ", luas)

        #Keliling
    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+"b. Keliling")
        sisi_kanan = float(input("masukan panjang sisi kanan: "))
        sisi_kiri = float(input("masukan panjang sisi kiri: "))
        sisi_bawah = float(input("masukan panjang sisi bawah/alas: "))

        keliling = sisi_kanan + sisi_kiri + sisi_bawah
        print("keliling segitiga Anda adalah: ", keliling)

elif pilihan == "lingkaran" or pilihan == "Lingkaran" or pilihan == "d" or pilihan == "D":
    #LINGKARAN
    print("\n\n", 3*"="+" 4 - LINGKARAN"+"="*3)
    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)
        #Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        jari_jari = float(input("masukan jari-jari: "))
        luas = 22/7 * jari_jari * jari_jari
        print("luas lingkaran Anda adalah: ", luas)

    #Keliling
    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+"b. Keliling")
        jari_jari = float(input("masukan panjang jari-jari: "))
        keliling = 22/7 * jari_jari ** 2
        print("keliling lingkaran Anda adalah: ", keliling)

elif pilihan == "trapesium" or pilihan == "Trapesium" or pilihan == "e" or pilihan == "E":
    #TRAPESIUM    
    print("\n\n", 3*"="+" 5 - TRAPESIUM"+"="*3)
    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)

        #Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        a = float(input("masukan panjang atas: "))
        b = float(input("masukan panjang bawah: "))
        t = float(input("masukan panjang tinggi: "))
        luas = a + b / 2 * t
        print("luas trapesium Anda adalah: ", luas)

        #Keliling
    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+"b. Keliling")
        sisi_samping = float(input("masukan panjang sisi samping: "))
        sisi_atas = float(input("masukan panjang sisi atas: "))
        sisi_bawah = float(input("masukan panjang sisi bawah: "))

        keliling = 2 * sisi_samping + sisi_atas + sisi_bawah
        print("keliling trapesium Anda adalah: ", keliling)

elif pilihan == "jajargenjang" or pilihan == "Jajargenjang" or pilihan == "f" or pilihan == "F":

    #JAJARGENJANG

    print("\n\n", 3*"="+" 6 - JAJARGENJANG"+"="*3)
    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)

    #Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        a = float(input("masukan panjang alas: "))
        t = float(input("masukan panjang tinggi: "))
        luas = a * t
        print("luas jajargenjang Anda adalah: ", luas)

    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        #Keliling
        print("\n", 3*"="+"b. Keliling")
        sisi_samping = float(input("masukan panjang sisi samping: "))
        sisi_atas_bawah = float(input("masukan panjang sisi atas atau bawah: "))
        keliling = 2 * (sisi_samping + sisi_atas_bawah)
        print("keliling jajargenjang Anda adalah: ", keliling)

elif pilihan == "layang-layang" or pilihan == "Layang-Layang" or pilihan == "LAYANG-LAYANG" or pilihan == "layang layang" or pilihan == "Layang Layang" or pilihan == "LAYANG LAYANG" or pilihan == "g" or pilihan == "G":

    #LAYANG-LAYANG
    print("\n\n", 3*"="+" 7 - LAYANG-LAYANG"+"="*3)
    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)

    #Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        d1 = float(input("masukan panjang diagonal pendek (d1): "))
        d2 = float(input("masukan panjang diagonal panjang (d2): "))
        luas = 1/2 * d1 * d2
        print("luas layang-layang Anda adalah: ", luas)

    #Keliling
    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+"b. Keliling")
        sisi_pendek = float(input("masukan panjang sisi pendek: "))
        sisi_panjang = float(input("masukan panjang sisi panjang: "))
        keliling = 2 * (sisi_pendek + sisi_panjang)
        print("keliling layang-layang Anda adalah: ", keliling)

elif pilihan == "belah ketupat" or pilihan == "Belah Ketupat" or pilihan == "BELAH KETUPAT" or pilihan == "h" or pilihan == "H":
    #BELAH KETUPAT
    print("\n\n", 3*"="+" 8 - BELAH KETUPAT"+"="*3)
    pilihan = input("""ingin mencari:
    a. luas
    b. keliling
    
    Jawaban Anda: """)   
    
    #Luas
    if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
        print(3*"="+"a. Luas")
        d1 = float(input("masukan panjang diagonal pendek (d1): "))
        d2 = float(input("masukan panjang diagonal panjang (d2): "))
        luas = 1/2 * d1 * d2
        print("luas belah ketupat Anda adalah: ", luas)

    #Keliling
    elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
        print("\n", 3*"="+"b. Keliling")
        sisi_pendek = float(input("masukan panjang sisi pendek: "))
        sisi_panjang = float(input("masukan panjang sisi panjang: "))
        keliling = 2 * (sisi_pendek + sisi_panjang)
        print("keliling belah ketupat Anda adalah: ", keliling)

else:
    print("Anda tidak memilih apapun")

print("\nProgram telah selesai. Terima Gajih!")
