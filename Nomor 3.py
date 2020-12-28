file = open("file.txt" , "r")

baris = file.readlines()
Dictionari = {}
listDictionari = []
for x in range(len(baris)):
    a = baris[x].split("|")
    a[2] = a[2].replace('\n', '')

    Dictionari = {'nama' : a[0], 'nim' : a[1], 'alamat' : a[2]}

    listDictionari.append(Dictionari)

print(listDictionari)
               
