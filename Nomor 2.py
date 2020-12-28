
file = open("file.txt", "a")

i = True
while ( i == True) :
    nim = input("Masukkan NIM : ")
    namaMhs = input("Masukkan Nama Mhs : ")
    alamat = input("Masukkan Alamat : ")

    file.write(nim + "|" + namaMhs + "|" + alamat + "\n")  
    ulang = input("Ulangi input lagi (y/n) : ")
    
    if (ulang == "y") :
        i = True
    elif  (ulang == "n"):
        i = False
    else :
        print ("Inputan anda tidak valid")
        continue
file.close()

