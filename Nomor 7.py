def decrypt(teks, n) :
    
    listTeks = list(teks)

    for x in range(len(listTeks)) :
        if(listTeks[x] != ' ') :
            if(ord(listTeks[x]) - n >= 65) :
                
                asciCode = ord(listTeks[x])
                decrypted = asciCode - n
                listTeks[x] = chr(decrypted)

            else :
                
                asciCode = ord(listTeks[x])
                decrypted = (asciCode + 26) - n
                listTeks[x] = chr(decrypted)

        else :
            
            continue

    result = ''.join(listTeks)

    return result


try :
    
    teks = input("Masukkan teks yang ingin anda enkripsi : ")
    n = int(input("Berapa geseran enkripsi : "))

    hasil = decrypt(teks, n)
    print("\nHasil pengenkripsian dari teks {0} adalah : {1}".format(teks, hasil))

except ValueError :
    print("Masukkan bilangan bulat!")
