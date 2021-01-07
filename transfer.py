from random import randint
import menu

def createCodeTransfer():
    random_number = 0
    range_start = 10**(3-1)
    range_end = (10**3)-1
    random_number = randint(range_start, range_end)
    norek = 'TRF' + str(random_number)
    return norek

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

def transfer():
    print("*** TRANSFER ***")
    data_nasabah = openFile()
    rek_sumber = input("Masukan nomor rekening sumber: ")
    rek_tujuan = input("Masukan nomor rekening tujuan: ")
    try:
        nominal_transfer = int(input("Masukan nominal yang akan ditransfer: "))
    except ValueError:
        print("nominal yang di isi harus dengan angka")
        return transfer()
    isRekSumber = False
    isRekTujuan = False
    i = 0
    code_trf = None
    while i < len(data_nasabah):
        if rek_sumber.upper() in data_nasabah[i]:
            index_sumber = i
            isRekSumber = True
        if rek_tujuan.upper() in data_nasabah[i]:
            index_tujuan = i
            isRekTujuan = True
        i = i + 1
    if isRekSumber == False:
        print("Nomor rekening sumber tidak terdaftar. Transfer gagal.")
    if isRekTujuan == False:
        print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.")
    elif isRekSumber == True and isRekTujuan == True:
        if int(data_nasabah[index_sumber][2]) >= nominal_transfer:
            code_trf = createCodeTransfer()
            saldo_sumber = int(data_nasabah[index_sumber][2]) - nominal_transfer
            saldo_tujuan = int(data_nasabah[index_tujuan][2]) + nominal_transfer
            data_nasabah[index_sumber][2] = data_nasabah[index_sumber][2].replace(data_nasabah[index_sumber][2], str(saldo_sumber))
            data_nasabah[index_tujuan][2] = data_nasabah[index_tujuan][2].replace(data_nasabah[index_tujuan][2], str(saldo_tujuan))
            print("Transfer sebesar {} dari rekening {} ke rekening {} berhasil".format(nominal_transfer, rek_sumber, rek_tujuan))
        else:
            print("Saldo tidak mencukupi. Transfer gagal")
    change_file = open('nasabah.txt', 'w+')
    for element in data_nasabah:
        element = str(element).replace('[', '').replace(']', '').replace("'", "").replace(' ', '')
        change_file.write(element + '\n')
    change_file.close()

    if code_trf is not None:
        data = code_trf + ',' + rek_sumber.upper() + ',' + rek_tujuan.upper() + ',' + str(nominal_transfer)
        data_transfer = open("transfer.txt", 'a+')
        data_transfer.write(str(data) + '\n')
    print()

    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()