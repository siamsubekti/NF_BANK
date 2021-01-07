import menu

def openFile():
    nasabah_list = []
    file = open("nasabah.txt")
    for each_line in file:
        data = each_line.split(',')
        rek = data[0]
        nama = data[1]
        data_saldo = data[2]
        saldo = data_saldo.split('\n')
        nasabah_list.append([rek, nama, saldo[0]])
    file.close()
    return nasabah_list

def tarik():
    data_nasabah = openFile()
    print("*** TARIK TUNAI ***")
    rek_nasabah = input("Masukan nomor rekening: ")
    try:
        nominal_tarik = int(input("Masukan nominal yang akan ditarik: "))
    except ValueError:
        print("nominal yang akan ditarik harus berisi angka")
        return tarik()
    counter = 0
    i = 0
    while i < len(data_nasabah):
        if rek_nasabah.upper() in data_nasabah[i]:
            if int(data_nasabah[i][2]) >= nominal_tarik:
                hasil = int(data_nasabah[i][2]) - nominal_tarik
                data_nasabah[i][2] = data_nasabah[i][2].replace(data_nasabah[i][2], str(hasil))
                print("Tarik tunai sebesar {} dari rekening {} berhasil".format(nominal_tarik, rek_nasabah))
            else:
                print("Saldo tidak mencukupi. Tarik tunai gagal.")
        else:
            counter = counter + 1
        i = i + 1
        if counter == len(data_nasabah):
            print("Nomor rekening tidak terdaftar. Tarik tunai gagal.")
        
        change_file = open('nasabah.txt', 'w+')
        for element in data_nasabah:
            element = str(element).replace('[', '').replace(']', '').replace("'", '').replace(" ", '')
            change_file.write(element + '\n')
        change_file.close()
    print()

    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()