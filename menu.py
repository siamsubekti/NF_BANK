import bukaRekening
import setorTunai
import tarikTunai
import transfer
import daftarTransfer

def selectInput():
    try:
        item = int(input("Masukan menu pilihan Anda: "))
        if (item <= 0) or (item > 6):
            print("Pilihan menu salah, silahakan ulangi.")
            return selectInput()
        else:
            return item
    except ValueError:
        print("Pilihan Anda salah. Ulangi")
        return selectInput()

def keluar():
    return print("Terima kasih atas kunjungan anda.")

def selectMenu(item):
    if item == 1:
        bukaRekening.buka()
    elif item == 2:
        setorTunai.setor()
    elif item == 3:
        tarikTunai.tarik()
    elif item == 4:
        return transfer.transfer()
    elif item == 5:
        return daftarTransfer.listTransfer()
    else:
        return keluar()

def mainMenu():
    print("""\
MENU:
[1] Buka Rekening
[2] Setoran Tunai
[3] Tarik Tunai
[4] Transfer
[5] Lihat daftar transfer
[6] Keluar\
""")
    # pilihan()
    item = selectInput()
    selectMenu(item)

if __name__ == "__main__":
    print("***** SELAMAT DATANG DI NF BANK *****")
    mainMenu()


