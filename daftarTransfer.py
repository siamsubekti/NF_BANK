import menu

def openFile():
    nasabah_list = []
    file = open('nasabah.txt')
    for each_line in file:
        data = each_line.split(',')
        rek = data[0]
        nama = data[1]
        data_saldo = data[2]
        saldo = data_saldo.split('\n')
        nasabah_list.append([rek, nama, saldo[0]])
    file.close()
    return nasabah_list

def openFileTransfer():
    transfer_list = []
    file = open('transfer.txt')
    for each_line in file:
        data = each_line.split(',')
        code = data[0]
        sumber = data[1]
        tujuan = data[2]
        nominal_saldo = data[3]
        nominal = nominal_saldo.split('\n')
        transfer_list.append([code, sumber, tujuan, nominal[0]])
    file.close()
    return transfer_list

def listTransfer():
    print("*** LIHAT DATA TRANSFER ***")
    data_nasabah = openFile()
    list_transfer = openFileTransfer()
    rek_sumber = input("Masukan nomor rekening sumber transfer: ")
    i = 0
    j = 0
    counter = 0
    daftar = []
    while i < len(data_nasabah):
        if rek_sumber.upper() in data_nasabah[i]:
            while j < len(list_transfer):
                if rek_sumber.upper() == list_transfer[j][1]:
                    daftar.append(list_transfer[j])
                j = j + 1
        else:
            counter = counter + 1
        i = i + 1
    if counter == len(data_nasabah):
        print("Nomor rekening sumber tidak terdaftar")
    else: 
        if daftar == []:
            print("Tidak ada data yang ditampilkan")
        else:
            print("Daftar transfer dari rekening {} :".format(rek_sumber))
            for element in daftar:
                element = str(element).replace('[', '').replace(']', '').replace("'", '').replace(',', '')
                print(element)
    print()

    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()