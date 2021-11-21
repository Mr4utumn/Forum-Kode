#Project ke 2
#membuat konsep dasar rumus bangun datar
print(10*"="+"APLIKASI BANGUN DATAR DAN RUANG"+"="*10 + "\n")

pilihan0 = input("""Ingin Mencari:
a. Bangun Datar
b. Bangun Ruang

Jawaban Anda: """)

# A. BANGUN DATAR
if pilihan0 == "a" or pilihan0 == "Bangun Datar" or pilihan0 == "A" or pilihan0 == "bangun datar":
    pilihan = input(""" Pilih salah satu bangun datar yang ingin dicari:
    a. Persegi
    b. Persegi Panjang
    c. Segitiga
    d. Lingkaran
    e. Trapesium
    f. Jajargenjang
    g. Layang-Layang
    h. Belah Ketupat

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

# B. BANGUN RUANG
elif pilihan0 == "b" or pilihan0 == "Bangun Ruang" or pilihan0 == "B" or pilihan0 == "bangun ruang":
    pilihan = input(""" Pilih salah satu bangun datar yang ingin dicari:
    a. Kubus
    b. Balok
    c. Limas Segitiga
    d. Limas Segi Empat
    e. Prisma Segitiga
    f. Tabung
    g. Kerucut
    h. Bola

    Jawaban Anda: """)
    # KUBUS
    if pilihan == "a" or pilihan == "A" or  pilihan == "kubus" or  pilihan == "Kubus" or  pilihan == "KUBUS":
        #KUBUS
        print(3*"="+" 1 - KUBUS "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")
            sisi = float(input("masukan panjang sisi(cm): "))
            luas = 6*(sisi * sisi)
            print("Luas Kubus adalah: ", luas)


        elif  pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")
            sisi = float(input("masukan panjang rusuk (cm): "))
            keliling = 12 * sisi
            print("keliling Kubus adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            sisi = float(input("masukan panjang sisi (cm): "))
            Volume = sisi**3
            print("Volume Kubus adalah: ", Volume)

    # BALOK
    if pilihan == "b" or pilihan == "B" or  pilihan == "balok" or  pilihan == "Balok" or  pilihan == "BALOK":
        
        print(3*"="+" 2 - BALOK "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            p = float(input("masukan panjang (cm): "))
            l = float(input("masukan lebar (cm): "))
            t = float(input("masukan tinggi (cm): "))
                        
            luas = 2*(p*l + l*t + p*t)
            print("Luas Balok adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            p = float(input("masukan panjang (cm): "))
            l = float(input("masukan lebar (cm): "))
            t = float(input("masukan tinggi (cm): "))

            keliling = 4*(p+l+t)
            print("keliling Balok adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            p = float(input("masukan panjang (cm): "))
            l = float(input("masukan lebar (cm): "))
            t = float(input("masukan tinggi (cm): "))
            Volume = p*l*t
            print("Volume Balok adalah: ", Volume)

    # LIMAS SEGITIGA
    if pilihan == "c" or pilihan == "C" or  pilihan == "limas segitiga" or  pilihan == "Limas Segitiga" or  pilihan == "LIMAS SEGITIGA":
        
        print(3*"="+" 3 - Limas Segitiga "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            luas_alas = float(input("masukan luas alas (cm): "))
            luas_selubung_limas = float(input("masukan luas selubung limas (cm): "))
                        
            luas = luas_alas * luas_selubung_limas
            print("Luas Limas Segitiga adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            keliling_alas = float(input("masukan panjang keliling alas (cm): "))
            rusuk_limas = float(input("masukan panjang rusuk limas (cm): "))

            keliling = keliling_alas + 3*rusuk_limas
            print("keliling Limas Segitiga adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            luas_alas = float(input("masukan luas alas (cm): "))
            tinggi = float(input("masukan tinggi (cm): "))
            
            Volume = 1/3 * luas_alas * tinggi
            print("Volume Limas Segitiga adalah: ", Volume)  
    
    # LIMAS SEGI EMPAT
    if pilihan == "d" or pilihan == "D" or  pilihan == "Limas Segi Empat" or  pilihan == "limas segi empat" or  pilihan == "LIMAS SEGI EMPAT":

        print(3*"="+" 4 - Limas Segi Empat "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            luas_alas = float(input("masukan luas alas (cm): "))
            luas_selubung_limas = float(input("masukan luas selubung limas (cm): "))
                        
            luas = luas_alas * luas_selubung_limas
            print("Luas Limas Segi Empat adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            keliling_alas = float(input("masukan panjang keliling alas (cm): "))
            rusuk_limas = float(input("masukan panjang rusuk limas (cm): "))

            keliling = keliling_alas + 4*rusuk_limas
            print("keliling Limas Segi Empat adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            luas_alas = float(input("masukan luas alas (cm): "))
            tinggi = float(input("masukan tinggi (cm): "))
            
            Volume = 1/3 * luas_alas * tinggi
            print("Volume Limas Segi Empat adalah: ", Volume)  

    # PRISMA SEGITIGA
    if pilihan == "e" or pilihan == "E" or  pilihan == "Prisma Segitiga" or  pilihan == "prisma segitiga" or  pilihan == "PRISMA SEGITIGA":

        print(3*"="+" 5 - Prisma Segitiga "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            keliling_alas = float(input("masukan keliling alas (cm): "))
            luas_alas = float(input("masukan luas alas (cm): "))
            tinggi_prisma = float(input("masukan tinggi Prisma (cm): "))
                        
            luas = keliling_alas * tinggi_prisma + 2 * luas_alas
            print("Luas Prisma Segitiga adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            keliling_alas = float(input("masukan panjang keliling alas (cm): "))
            rusuk_limas = float(input("masukan panjang rusuk limas (cm): "))

            keliling = 2 * keliling_alas + 4 * rusuk_limas
            print("keliling Prisma Segitiga adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            luas_alas = float(input("masukan luas alas (cm): "))
            tinggi = float(input("masukan tinggi (cm): "))
            
            Volume = luas_alas * tinggi
            print("Volume Prisma Segitiga adalah: ", Volume)  

    # LIMAS
    if pilihan == "f" or pilihan == "F" or  pilihan == "Limas" or  pilihan == "limas" or  pilihan == "LIMAS":

        print(3*"="+" 5 - Limas "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            keliling_alas = float(input("masukan keliling alas (cm): "))
            luas_alas = float(input("masukan luas alas (cm): "))
            tinggi_tabung = float(input("masukan tinggi Prisma (cm): "))
                        
            luas = 2 * luas_alas + tinggi_prisma  * keliling_alas
            print("Luas Limas adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            jari_jari = float(input("masukan panjang jari-jari (cm): "))

            keliling = 2 * 22/7 * jari_jari
            print("keliling Limas adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            jari_jari = float(input("masukan panjang jari_jari (cm): "))
            tinggi = float(input("masukan tinggi (cm): "))
            
            Volume = 22/7 * jari_jari**2 * tinggi
            print("Volume Limas adalah: ", Volume)  

    # KERUCUT
    if pilihan == "g" or pilihan == "G" or  pilihan == "Kerucut" or  pilihan == "kerucut" or  pilihan == "KERUCUT":

        print(3*"="+" 5 - Kerucut "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            jari_jari = float(input("masukan panjang jari-jari (cm): "))
            tinggi = float(input("masukan tinggi kerucut (cm): "))

            luas = 22/7 * jari_jari * (jari_jari + tinggi)
            print("Luas Kerucut adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            jari_jari = float(input("masukan panjang jari-jari (cm): "))

            keliling = 2 * 22/7 * jari_jari
            print("keliling Kerucut adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")
            jari_jari = float(input("masukan panjang jari_jari (cm): "))
            tinggi = float(input("masukan tinggi (cm): "))
            
            Volume = 1/3 * 22/7 * jari_jari**2 * tinggi
            print("Volume Kerucut adalah: ", Volume)  

    # BOLA
    if pilihan == "h" or pilihan == "H" or  pilihan == "bola" or  pilihan == "Bola" or  pilihan == "BOLA":

        print(3*"="+" 5 - Bola "+"="*3)

        pilihan = input("""ingin mencari:
        a. luas
        b. keliling
        c. volume
        
        Jawaban Anda: """)

        if pilihan=="luas" or pilihan == "a" or pilihan == "LUAS" or pilihan == "A":
            print(3*"="+" a. Luas")

            jari_jari = float(input("masukan panjang jari-jari (cm): "))
            
            luas = 4 * 22/7 * jari_jari**2
            print("Luas Bola adalah: ", luas)


        elif pilihan=="keliling" or pilihan == "b" or pilihan == "KELILING" or pilihan == "B":
            print("\n", 3*"="+" b. Keliling")

            jari_jari = float(input("masukan panjang jari-jari (cm): "))

            keliling = 4/3 * 22/7 * jari_jari**2
            print("keliling Bola adalah: ", keliling)
        
        elif pilihan=="volume" or pilihan=="Volume" or pilihan=="VOLUME" or pilihan=="c" or pilihan=="C":
            print("\n", 3*"="+" c. Volume")

            jari_jari = float(input("masukan panjang jari_jari (cm): "))
            
            Volume = 4 * 22/7 * jari_jari**3
            print("Volume Bola adalah: ", Volume)  

else:
    print("Anda tidak memilih apapun")

print("\nProgram telah selesai. Terima Gajih!")
