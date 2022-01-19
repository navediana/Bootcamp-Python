pilihan="y" 
while pilihan=="y":

    print("Kategori_Jasa: ")
    print("      1. Express     (15000/kg, 2 hari)")
    print("      2. Biasa       (6000/kg, 7 hari)")
    print("      3. Cuci        (5000/kg, 5 hari)")
    print("      4. Setrika     (5000/kg, 5 hari)")
    print("      5. Cuci + Setrika (10000/kg, 4 hari)")
    pilihan=int(input("Silahkan Masukkan Pilihan Anda: "))
    print()


    print(".................Inputan Data Sahabat In Love................")
    tml=str(input("Tanggal Laundry Masuk : "))
    tkl=str(input("Tanggal Laundry Diambil : "))
    nama=str(input("Nama Pelanggan       : "))
    alt=str(input("Alamat                : "))
    nhp=int(input("No Handphone          :"))
    berat=int(input("Berat Laundry         :  "))

    if pilihan == 1:
        jenis= "Express"
        harga=(15000*berat)
        if berat > 7:
            diskon = int(harga*0.1)
            total=int(harga-diskon)
        elif berat >= 5:
            diskon = int(harga * 0.05)
            total =int(harga-diskon)
        else:
            diskon =(0)
            total =int(harga)
            
    elif pilihan == 2:
        jenis= "Biasa"
        harga = (6000*berat)
        if berat >= 5:
            diskon = int(harga * 0.05)
            total =int(harga-diskon)
        else:
            diskon =(0)
            total =int(harga)
            
    elif pilihan == 3:
        jenis= "Cuci"
        harga = (5000*berat)
        if berat >= 5:
            diskon = int(harga * 0.05)
            total =int(harga-diskon)
        else:
            diskon =(0)
            total =int(harga)
           
    elif pilihan == 4:
        jenis= "Setrika"
        harga = (5000*berat)
        if berat >= 5:
            diskon = int(harga * 0.05)
            total =int(harga-diskon)
        else:
            diskon =(0)
            total =int(harga)
           
    elif pilihan == 5:
        jenis= "Cuci + Setrika"
        harga = (10000*berat)
        if berat > 7:
            diskon = int(harga * 0.1)
            total =int(harga-diskon)
        elif berat >= 5:
            diskon = int(harga * 0.05)
            total =int(harga-diskon)
        else:
            diskon =(0)
            total =int(harga)

    
    else:
        jenis = "-"
        harga = "-"
        diskon = "-"
        total = "-"
        pilihan=input("Maaf, Sahabat salah pilih! Silahkan masukkan pilihan yang benar.  Y/N :")

    print()
    def Data():
        print("=================================================================")
        print("                LAUNDRY IN lOVE UNIVERSISTI")
        print("                  Kota Campus di Colorday")
        print("              Jl In Love Bareng No.210 Campus 1")
        print("=================================================================")
        print()
        print("Tanggal Masuk       :",tml)
        print("Tanggal Diambil     :",tkl)
        print("Nama Pelanggan      :",nama)
        print("Alamat              :",alt)
        print("Nomor Hp            :",nhp)
        print("Layanan             :",jenis)
        print("Berat Laundry       :",berat)
        print("Harga               :",harga)
        print("Diskon              :",diskon)
        print("====================")
        print("Harga yang dibayar  :",total)
        print("====================")
        print("                                                         TTD")
        print("                                                lOVE IN UNIVERSISTI")
        print()
    Data()
    pilihan=input(" Sahabat mulai Laundry in lagi ??? Y / N :  ")
