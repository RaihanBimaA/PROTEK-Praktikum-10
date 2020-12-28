file = open('isifiletext.txt', 'r')

IsiFileAngka = file.readlines()

angkaGenap = []
angkaGanjil = []

for x in range(len(IsiFileAngka)):
    if ('\n' in IsiFileAngka[x] == True):
        IsiFileAngka[x].replace('\n', '')

        if (int(IsiFileAngka[x])%2 == 0):
            angkaGenap.append(IsiFileAngka[x])
        else :
            angkaGanjil.append(IsiFileAngka[x])
    else :
        if (int(IsiFileAngka[x])%2 == 0) :
            angkaGenap.append(IsiFileAngka[x])
        else :
            angkaGanjil.append(IsiFileAngka[x])

print ("Banyaknya bilangan Genap : {0}".format(len(angkaGenap)))
print ("Banyaknya bilangan Genap : {0}".format(len(angkaGanjil)))
