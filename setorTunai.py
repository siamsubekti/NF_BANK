import menu

def openFile():
    nasabah_list = []
    file = open('nasabah.txt')
    for each_line in file:
        data = each_line.split(',')
        rek = data[0]
        nama = data[1]
        dataSaldo = data[2]
        saldo = dataSaldo.split('\n')
        nasabah_list.append([rek, nama, saldo[0]])
    file.close()
    return nasabah_list

def setor():
    data_nasabah = openFile()
    print("*** SETORAN TUNAI ***")
    rek_nasabah = input("Masukan nomor rekening: ")
    try:
        nominal_setor = int(input("Masukan nominal yang akan disetor: "))
    except ValueError:
        print("nominal harus berisi angka")
        return setor()
    counter = 0
    i = 0
    while i < len(data_nasabah):
        if rek_nasabah.upper() in data_nasabah[i]:
            hasil = int(data_nasabah[i][2]) + nominal_setor
            data_nasabah[i][2] = data_nasabah[i][2].replace(data_nasabah[i][2], str(hasil))
            print("Setoran tunai sebesar {} ke rekening {} berhasil".format(nominal_setor, rek_nasabah))
        else:
            counter = counter + 1
        i = i + 1
    if counter == len(data_nasabah):
        print("Nomor rekening tidak terdaftar. Setoran tunai gagal")

    change_file = open('nasabah.txt', 'w+')
    for element in data_nasabah:
        element = str(element).replace('[', '').replace(']', '').replace("'", "").replace(" ", "")
        change_file.write(element + '\n')
    change_file.close()
    print()

    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()