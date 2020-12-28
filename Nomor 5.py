file= open ('penjumlahan.txt','r')
isiFile= file.readlines()
for x in range(len(isiFile)):
    replaced=isiFile[x].replace('\n','')
    splited=replaced.split('|')
    hasil=int(splited[0])+int(splited[1])
    isiFile[x]=hasil
print (isiFile)
file.close()
file2=open('hasilPenjumlahan','w')
for i in range (len(isiFile)):
    file2.write(str(isiFile[i])+'\n')
file2.close()
