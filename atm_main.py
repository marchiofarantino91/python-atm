import random
import datetime
from customer import Customer

atm  = Customer(id)

while True:
     id = int(input("masukan pin anda:"))

     trial=0
     
     while (id != int(atm.getCustPin()) and trial < 3):
          id = int(input(" Pin ada salah.  silakan masukkan lagi  :")) 
          trial+=1

          if trial ==3:
               print("Error,  silakan ambil kartu dan coba lagi. . ")
               exit()
     while True:         
          print("selamat datang di aplikasi ATM ..")
          print("\n1 - Cek Saldo \t 2- Debet \t 3 - Simpan \t 4 - Ganti Pin  |\t 5 - Keluar ")

          menu = int( input("\n Silakan pilih menu: "))

          if menu == 1 :
               print("\Saldo anda sekarang: Rp.  " + str(atm.getCustBalance()) + "\n")

               elif menu ==2:
                    bal = float(input("Masukan nominal saldo: "))
                    verifyBal = input( "Anda akan melakukan penarikan sebesar Rp. "+ str(bal)+" Apakah anda ingin melanjutkan? \t 1.Ya \t 2. Tidak ")
                    
                    if verifyBal == 1:
                         print("Saldo anda saat ini : Rp. "+ str(atm.getCustBalance()))
                    else: break

                    if bal < atm.getCustBalance():
                         atm.withdraw(bal )
                         print("transaksi berhasil!\n Saldo anda saat ini : Rp. " + str(atm.getCustBalance())) 
                    else:
                         print( " maaf,  saldo anda tidak mencukupi.  ")     




               elif menu ==3:
               elif menu ==4:
               elif menu ==5:
               else:








