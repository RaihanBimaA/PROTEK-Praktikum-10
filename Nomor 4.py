fileMhs = open("file.txt" , "r")
nim= input('Masukkan NIM yang mau dicari:')
isiFile=fileMhs.readlines()
for x in range(len(isiFile)):
    if(nim in isiFile[x]):
        status='Ada'
        break
    else:
        status='Tidak Ada'
        continue
if(status=='Ada'):
    splited=isiFile[x].split('|')
    print('Data Mahasiswa')
    print('NIM:',splited[0])
    print('Nama:',splited[1])
    print('Alamat:',splited[2])
else:
    print('Data Mahasiswa Tidak Ditemukan')
