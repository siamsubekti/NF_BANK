from random import randint
import menu

def createRekening():
    random_number = 0
    range_start = 10**(3-1)
    range_end = (10**3)-1
    random_number = randint(range_start, range_end)
    norek = 'REK' + str(random_number)
    return norek

def buka():
    print("*** BUKA REKENING ***")
    input_nama = input("Masukan nama: ")
    try:
        input_setor_awal = int(input("Masukan setoran awal: "))
        if input_setor_awal != 0:
            rek = createRekening()
        else:
            print("Setoran tidak boleh kosong")
            return buka()
    except ValueError:
        print("setoran awal hanya dapat diisi angka")
        return buka()
    
    data = rek + ',' + input_nama + ',' + str(input_setor_awal)
    data_nasabah = open("nasabah.txt", 'a+')
    data_nasabah.write(str(data) + '\n')
    print("Pembukaan rekening dengan nomor {} atas nama {} berhasil".format(rek, input_nama))
    print()

    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()