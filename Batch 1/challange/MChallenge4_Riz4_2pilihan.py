#Mini Challenge4 Bootcamp Python 21
print("=============================================================================")
print("___________________APLIKASI LAUNDRY IN lOVE UNIVERSISTI______________________")
print("                     Cepat, Bersih, Nyaman, dan Harum")
print("=============================================================================")
print()
print()

print("Selamat Datang Di Layanan Sahabat In Love LAUNDRY IN lOVE UNIVERSISTI")
print()
print("Percayakan layanamu untuk tampil indah bersama LAUNDRY IN lOVE UNIVERSISTI.... ")
print()
print("    Sebagai tanda terimakasih atas kesetiaannya kepada Sahabat In Love,")
print(" Laundry In Love Universisti memberikan diskon 5% bagi Sahabat In Love dengan berat Laundry 5kg")
print(" dan diskon sebesar 10% untuk Sahabat In Love yang memilih layanan Express Cuci + Setrika dengan berat lebih dari 7Kg")
print()


tml = ""
tkl =""
nama = ""
alt = ""
nhp = ""
jenis = ""
jumlah = ""
harga = ""
diskon = ""
total = ""

def menu():

    global tml, tkl, nama, alt, nhp, jenis, jumlah, harga, diskon, total

    pesan = str(input('''
    Kategori Pelayanan :
    
        1. Express (10000, 2 hari)
        2. Biasa   (6000, 5 hari)
    
    Kategori Jasa :
    
        A. Cuci             (5000/kg)
        B. Setrika          (5000/kg)
        C. Cuci + Setrika   (10000/kg)
        
    Contoh : (Pelayanan.Jasa) =>> 1.B
    
    Silahkan Masukan Pilihan Anda =>> '''))

    print()
    print(".................Inputan Data Sahabat In Love................\n")
    tml = str(input("Tanggal Laundry Masuk  : "))
    tkl=str(input("Tanggal Laundry Diambil : "))
    nama = str(input("Nama Pelanggan         : "))
    alt = str(input("Alamat                 : "))
    nhp = int(input("No Handphone           : "))
    jumlah = int(input("Berat Laundry          : "))

    if pesan == "1.A" or pesan == "1.a":
        jenis = "Express & Cuci"
        harga = int((10000 + 5000) * jumlah)

        if jumlah >7:
            diskon = int(harga * 0.1)
            total = int(harga - diskon)
            hasil()
        else:
            diskon = (0)
            total = int(harga)
            hasil()

    elif pesan == "2.A" or pesan == "2.a":
        jenis = "Biasa & Cuci"
        harga = int((6000 + 5000) * jumlah)

        if jumlah >= 5:
            diskon = int(harga * 0.05)
            total = int(harga - diskon)
            hasil()
        else:
            diskon = (0)
            total = int(harga)
            hasil()

    elif pesan == "1.B" or pesan == "1.b":
        jenis = " Express & Setrika"
        harga = int((10000 + 5000) * jumlah)

        if jumlah >= 5:
            diskon = int(harga * 0.05)
            total = int(harga - diskon)
            hasil()
        else:
            diskon = (0)
            total = int(harga)
            hasil()

    elif pesan == "2.B" or pesan == "2.b":
        jenis = "Biasa & Setrika"
        harga = int((6000 + 5000) * jumlah)

        if jumlah >= 5:
            diskon = int(harga * 0.05)
            total = int(harga - diskon)
            hasil()
        else:
            diskon = (0)
            total = int(harga)
            hasil()

    elif pesan == "1.C" or pesan == "1.c":
        jenis = "Express Cuci & Setrika"
        harga = int((10000 + 10000) * jumlah)

        if jumlah > 7:
            diskon = int(harga * 0.1)
            total = int(harga - diskon)
            hasil()
        elif jumlah >= 5:
            diskon = int(harga * 0.05)
            total =int(harga-diskon)
            hasil()
        else:
            diskon = (0)
            total = int(harga)
            hasil()

    elif pesan == "2.C" or pesan == "2.c":
        jenis = "Biasa Cuci & Setrika"
        harga = int((6000 + 10000) * jumlah)
        if jumlah >= 5:
            diskon = int(harga * 0.05)
            total = int(harga - diskon)
            hasil()
        else:
            diskon = (0)
            total = int(harga)
            hasil()

    else:
        jenis = "-"
        harga = "-"
        diskon = "-"
        total = "-"
        pilihan = input("Maaf, keyword salah! silahkan masukkan nomor urut kembali.  Yes/No =>> ")

        if pilihan == "yes" or pilihan == 'Yes':
            menu()
        else:
            exit()

def hasil():

    global tml, tkl, nama, alt, nhp, jenis, jumlah, harga, diskon, total

    print()

    print("=================================================================")
    print("                LAUNDRY IN lOVE UNIVERSISTI")
    print("                  Kota Campus di Colorday")
    print("              Jl In Love Bareng No.210 Campus 1")
    print("=================================================================")
    print()
    print("Tanggal Masuk       :", tml)
    print("Tanggal Diambil    :",    tkl)
    print("Nama Pelanggan      :", nama)
    print("Alamat              :", alt)
    print("Nomor Hp            :", nhp)
    print("Layanan             :", jenis)
    print("Berat Laundry       :", jumlah)
    print("Harga               :", harga)
    print("Diskon              :", diskon)
    print("====================")
    print("Harga yang dibayar  :", total)
    print("====================")
    print("                                                         TTD")
    print("                                                lOVE IN UNIVERSISTI")
    print()
    pilihan = input("apakah ada Laundry an lain ? Yes / No =>> ")

    if pilihan == "yes" or pilihan == 'Yes':
        menu()
    else:
        exit()

menu()