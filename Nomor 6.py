def encrypt(teks, n) :
    
    listTeks = list(teks)

    for x in range(len(listTeks)) :
        if(listTeks[x] != ' ') :
            if(ord(listTeks[x]) + n < 90) :
                
                asciCode = ord(listTeks[x])
                encrypted = asciCode + n
                listTeks[x] = chr(encrypted)

            else :
                
                asciCode = ord(listTeks[x])
                encrypted = (asciCode + n) - 26
                listTeks[x] = chr(encrypted)

        else :
            
            continue

    result = ''.join(listTeks)

    return result


try :
    
    teks = input("Masukkan teks yang ingin anda enkripsi : ")
    n = int(input("Berapa geseran enkripsi : "))

    hasil = encrypt(teks, n)
    print("\nHasil pengenkripsian dari teks {0} adalah : {1}".format(teks, hasil))

except ValueError :
    print("Masukkan hanya bilangan bulat")
