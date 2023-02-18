dataSiswa = [
    {
        'Nim': 250,
        'Nama': 'Beni',
        'Sex': 'L',
        'Tempat lahir' : 'Bekasi',
        'Alamat' : 'Jl. Cempaka'
    },
    {
        'Nim': 251,
        'Nama': 'Siti',
        'Sex': 'P',
        'Tempat lahir' : 'Jakarta',
        'Alamat' : 'Jl. Cendrawasih'
    },
    {
        'Nim': 252,
        'Nama': 'Andi',
        'Sex': 'L',
        'Tempat lahir' : 'Depok',
        'Alamat' : 'Jl. Kutilang'
    }
]

# Pilihan Untuk menampilkan seluruh Data Siswa
def DaftarSiswa():
    print('''
                = = = = = Report Data Siswa = = = = =
                      = = = = SDN 4 Pagi = = = =\n''')
             
    print('''No \t| Nim \t| Nama   \t\t| Sex \t| Tempat Lahir \t| Alamat''')
    for i in range(len(dataSiswa)):
        print('{} \t| {} \t| {}   \t\t| {} \t| {} \t| {}'.format(i+1,dataSiswa[i]['Nim'],dataSiswa[i]['Nama'],dataSiswa[i]['Sex'],dataSiswa[i]['Tempat lahir'],dataSiswa[i]['Alamat']))

# Pilihan Menu No. 1 Report Data Siswa (Read)
def MenuDataSiswa():
    while True:
        print('''
        ===== Menu Report Data Siswa =====

         1. Menampilkan semua data siswa
         2. Menampilkan data tertentu
         3. Kembali ke Menu utama\n''')
         
        SubMenu = int(input('''Silahkan pilih daftar diatas [1-3] : '''))
        if SubMenu == 1 :
            DaftarSiswa()
        elif SubMenu == 2:
            UnikData ()
        elif SubMenu == 3:
            Menu_Awal()
        else :
            print('Anda memasukkan pilihan yang salah\nSilahkan masukkan pilihan Menu yang benar (1-3): ')
            continue

# Pilihan No 1.2 Menampilkan data tertentu
def UnikData ():
    inputNim = int(input('''
        Masukkan Nim siswa : '''))
    for i in range (len(dataSiswa)):
        if inputNim == dataSiswa[i]['Nim']:
            print(f'''\n\t\t=== Data siswa ditemukan ===\n
    === Siswa dengan Nim : {inputNim} datanya adalah sebagai berikut ===\n
                === Data Siswa SDN 4 Pagi ===\n''')
            print('No. \t|Nim \t| Nama   \t| Sex \t| Tempat Lahir \t| Alamat')
            print(f'''{i+1} \t| {dataSiswa[i]['Nim']} \t| {dataSiswa[i]['Nama']}   \t| {dataSiswa[i]['Sex']} \t| {dataSiswa[i]['Tempat lahir']} \t| {dataSiswa[i]['Alamat']}''')
            break
        elif (i == len(dataSiswa)-1) and (inputNim != dataSiswa[i]['Nim']):
            print('''\n\t\t=== Data siswa tidak ditemukan ===''')

# Pilihan Menu No. 2 Menambahkan Data Siswa (create)
def TambahData ():
    while True:
        CreateDataSiswa = input('''
        ===== Menu Menambah Data Siswa =====

            1. Tambah data siswa
            2. Kembali ke menu utama

        Silahkan pilih menu update data diatas [1-2] : ''')
        
        if CreateDataSiswa == '1':
            DaftarSiswa()
            NimSiswa = int(input('\nMasukkan Nim baru : '))
            for i in range(len(dataSiswa)):
                if NimSiswa == dataSiswa [i]['Nim']:
                        print('''
                === Data siswa sudah ada di Database ===
                === Silahkan masukkan data baru === ''')
                        TambahData() 
                elif (i == len(dataSiswa)-1) and NimSiswa != dataSiswa[i]['Nim'] :
                     NamaSiswa = input('Nama : ').capitalize()
                     SexSiswa = input('Sex : ').capitalize()
                     TempatLahirSiswa = input('Tempat lahir : ').capitalize()
                     AlamatSiswa = input('Alamat :').capitalize()
                     break
            Konfirmasi = input('''
                === Apakah data ini akan ditambahkan (Y/T)?: ''').capitalize()
            if Konfirmasi == 'Y':
                dataSiswa.append({
                    'Nim': NimSiswa,
                    'Nama': NamaSiswa,
                    'Sex': SexSiswa,
                    'Tempat lahir' : TempatLahirSiswa,
                    'Alamat' : AlamatSiswa
                    })
                print('\n=== Data siswa berhasil ditambahkan ===')
                DaftarSiswa()
                TambahData()
                continue
            elif Konfirmasi == 'T':
                print('\n=== Data siswa tidak jadi ditambahkan ===')
                TambahData() 
            else:
                    print('''\n=== Pilihan yang anda masukkan salah ===
                === Silahkan masukkan kembali pilihan yang benar (Y/T):''')
            TambahData()
        elif CreateDataSiswa == '2':
            Menu_Awal()
        else:
            print('''
    === Pilihan yang anda masukkan salah ===
    === Silahkan masukkan kembali pilihan yang benar (1-2):''')
            continue

# Pilihan Menu No. 3 Mengubah Data Siswa (update)
def UpdateData():
    while True:
        UpdateDataSiswa = input('''
        ===== Menu Ubah Data Siswa =====

            1. Ubah data siswa
            2. Kembali ke menu utama

        Silahkan pilih menu update data diatas [1-2] : ''')
        
        if UpdateDataSiswa == '1':
            DaftarSiswa()
            NimSiswa = (int(input('\n\t=== Masukkan Nim siswa: ')))
            for i in range(len(dataSiswa)):
                if NimSiswa == dataSiswa[i]['Nim'] :
                    while True:
                        print('''
                        === Data siswa ditemukan ===\n''')
                        print('''No.\t| Nim \t| Nama  \t| Sex \t| Tempat Lahir \t| Alamat''')
                        print(f'''{i+1} \t| {dataSiswa[i]['Nim']} \t| {dataSiswa[i]['Nama']}  \t| {dataSiswa[i]['Sex']} \t| {dataSiswa[i]['Tempat lahir']} \t| {dataSiswa[i]['Alamat']}''') 
                        Konfirmasi = input('''
                        === Apakah data ingin diubah (Y/T)?: ''').capitalize()
                        if Konfirmasi == 'Y' :
                            ubah_kolom = input('Pilih kolom yang ingin di ubah (Nim, Nama, Sex, Tempat lahir, Alamat): ').lower()
                            if ubah_kolom == dataSiswa[i]['Nim'] :
                               ubah_kolom = ubah_kolom.upper()
                            else:
                                ubah_kolom = ubah_kolom.capitalize()                                    
                            ubah_isi = input(f'Masukkan {ubah_kolom} baru : ').capitalize()
                            while True:
                                Konfirmasi1 = input('Apakah data jadi diubah(Y/T): ').capitalize()
                                if Konfirmasi1 == 'Y':
                                    dataSiswa[i][ubah_kolom] = ubah_isi
                                    print('''
                                \n\t\t=== Data sudah diubah ===''')
                                    DaftarSiswa()
                                    UpdateData()
                        elif Konfirmasi == 'T':
                            print(''' === Data siswa tidak jadi diubah ===''')
                            UpdateData()
                        else:
                            print('Masukkan (Y/T) saja')
                            break  
                elif (i == len(dataSiswa)-1) and (NimSiswa != dataSiswa[i]['Nim']) :
                    print('''
                    === Data siswa tidak ditemukan ===''')
                    
        elif UpdateDataSiswa == '2':
            Menu_Awal()
        else:
            print('''
    === Pilihan yang anda masukkan salah ===
    === Silahkan masukkan kembali pilihan yang benar (1-2):''')
            continue

# Pilihan Menu No. 4 Menghapus Data Siswa (Delete)
def DeleteData():
    DaftarSiswa()
    while True:
        DeleteDataSiswa = input('''
    === Menu Menghapus Data Siswa ===
        1. Hapus data siswa
        2. Kembali ke menu utama

    Silahkan pilih menu hapus data diatas [1-2] : ''')
        if DeleteDataSiswa == '1':
            NimSiswa = int(input('''
    === Masukkan Nim siswa yang akan dihapus datanya: '''))
            for i in range(len(dataSiswa)):
                if NimSiswa == dataSiswa[i]['Nim']:
                    while True :
                        print(''''
                === Data siswa ditemukan  ===\n''')
                        print('''No.\t| Nim \t| Nama  \t| Sex \t| Tempat Lahir \t| Alamat''')
                        print(f'''{i+1} \t| {dataSiswa[i]['Nim']} \t| {dataSiswa[i]['Nama']}  \t| {dataSiswa[i]['Sex']} \t| {dataSiswa[i]['Tempat lahir']} \t| {dataSiswa[i]['Alamat']}''') 
                        while True :
                            konfirmasi = input('''
    === Apakah anda yakin untuk menghapus data siswa ini (Y/T)? ''').capitalize()
                            if konfirmasi == 'Y':
                                del dataSiswa[i]
                                print(f'''
    === Data siswa dengan Nim : {NimSiswa} berhasil dihapus ===''')
                                DaftarSiswa()
                            elif konfirmasi == 'T':
                                print('''
    === Data siswa tidak dihapus ===''')
                            else:
                                print('''
    === Pilihan yang anda masukkan salah ===
    === Silahkan masukkan kembali pilihan yang benar (Y/T): ''')
                            Menu_Awal()
                
                elif  (i == len(dataSiswa)-1):
                    print(''''
                === Data siswa tidak ditemukan  ===\n''')
                    DeleteData() 
        elif DeleteDataSiswa == '2':
            Menu_Awal()
        else:
            print('''
    === Pilihan yang anda masukkan salah ===
    === Silahkan masukkan kembali pilihan yang benar (1-2):''')
            continue

# MENU UTAMA:
def Menu_Awal():
    print('''
= = = = = selamat datang di SDN 4 Pagi = = = = =
        
    = = = = = Daftar pilihan : = = = = =

        1. Report Data Siswa
        2. Menambahkan Data Siswa
        3. Mengubah Data Siswa
        4. Menghapus Data Siswa
        5. Exit ''')
   
    while True :
        PilihanMenu = input('\nMasukkan nomor yang dipilih (1-5): ')
        if PilihanMenu == '1':
            MenuDataSiswa()     
        elif PilihanMenu == '2' :
            TambahData()
        elif PilihanMenu == '3' :
            UpdateData()
        elif PilihanMenu == '4' :
            DeleteData()
        elif PilihanMenu == '5' :
            print('\n=== Terimakasih dan Sampai Jumpa Lagi :) ===\n')
            exit()
        else:
            print('Anda memasukkan pilihan yang salah\nSilahkan masukkan pilihan Menu yang benar (1-5) ')
            
# Menjalankan Program            
Menu_Awal()
