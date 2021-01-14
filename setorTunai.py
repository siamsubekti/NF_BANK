import menu

def setor():
    print(end="\n")
    print("from abdulloh")
    print("*** SETORAN TUNAI ***")

    listNasabah = []
    nasabah = open('nasabah.txt')
    for each_line in nasabah:
        data = each_line.split(',')
        rekNum = data[0]
        name = data[1]
        balance = eval(data[2])
        listNasabah.append([rekNum, name, balance])
    nasabah.close()

    recNumber = input('Masukkan nomor rekening: ')
    try:
        nominalDeposit = int(input('Masukkan nominal yang akan disetor: '))
    except ValueError:
        print("Nominal setor harus berisi angka!")
        return setor()
    
    counter = 0
    for i in range(len(listNasabah)):
        if(listNasabah[i][0].lower() == recNumber.lower()):
            totalDeposit = listNasabah[i][2] + nominalDeposit
            listNasabah[i][2] = totalDeposit
            print('Setoran tunai sebesar', nominalDeposit, 'ke rekening', recNumber.upper(), 'berhasil.')
        else: 
            counter += 1

    if counter == len(listNasabah):
        print('Nomor rekening tidak terdaftar. Setoran tunai gagal')
    nasabah = open('nasabah.txt', 'w+')
    for element in listNasabah:
        itemElement = str(element).replace('[','').replace(']','').replace("'",'').replace(' ', '')
        nasabah.write(itemElement + '\n')
    nasabah.close()
        
    print(end='\n')
    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()


# import menu

# def openFile():
#     nasabah_list = []
#     file = open('nasabah.txt')
#     for each_line in file:
#         data = each_line.split(',')
#         rek = data[0]
#         nama = data[1]
#         dataSaldo = data[2]
#         saldo = dataSaldo.split('\n')
#         nasabah_list.append([rek, nama, saldo[0]])
#     file.close()
#     return nasabah_list

# def setor():
#     data_nasabah = openFile()
#     print("*** SETORAN TUNAI ***")
#     rek_nasabah = input("Masukan nomor rekening: ")
#     try:
#         nominal_setor = int(input("Masukan nominal yang akan disetor: "))
#     except ValueError:
#         print("nominal harus berisi angka")
#         return setor()
#     counter = 0
#     i = 0
#     while i < len(data_nasabah):
#         if rek_nasabah.upper() in data_nasabah[i]:
#             hasil = int(data_nasabah[i][2]) + nominal_setor
#             data_nasabah[i][2] = data_nasabah[i][2].replace(data_nasabah[i][2], str(hasil))
#             print("Setoran tunai sebesar {} ke rekening {} berhasil".format(nominal_setor, rek_nasabah))
#         else:
#             counter = counter + 1
#         i = i + 1
#     if counter == len(data_nasabah):
#         print("Nomor rekening tidak terdaftar. Setoran tunai gagal")

#     change_file = open('nasabah.txt', 'w+')
#     for element in data_nasabah:
#         element = str(element).replace('[', '').replace(']', '').replace("'", "").replace(" ", "")
#         change_file.write(element + '\n')
#     change_file.close()
#     print()

#     # balik dan cetak list menu kembali untuk memilih menu,
#     # jika menu ini sudah selesai dilakukan.
#     menu.mainMenu()