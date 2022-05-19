import datetime
waktu = datetime.date.today()
year = waktu.year
month = waktu.month
day = waktu.day
while True:
        if day<10:
                day='0{0}'.format(day)
                if month<10:
                        month='0{0}'.format(month)
                        break
                else:
                        month=month
                        break
                break
        else:
                if month<10:
                        month='0{0}'.format(month)
                        break
                else:
                        month=month
                        break
                day=day
                break
hariini='{0}-{1}-{2}'.format(day,month,year)

ListKTP = []
choice = 1
while choice != 4:
    print()
    print('-----------------------------')
    print('SELAMAT DATANG DI PROGRAM KTP')
    print('-----------------------------')
    print()
    print('>>>> SILAHKAN PILIH MENU <<<<')
    print()
    print('-----------------------------')
    print('[1] Input Data KTP           ')
    print('[2] Lihat Data KTP           ')
    print('[3] Hapus Data KTP           ')
    print('[4] Selesai                  ')
    print('-----------------------------')
    print()

    choice = int(input('Masukan pilihan (1/2/3/4) : '))
    if choice == 1 :
        print()
        print('Anda memilih [1] Input Data KTP ')
        print()
        class KTP:
            def __init__(self,NIK,Nama,TempatLahir,TanggalLahir,JenisKelamin,GolonganDarah,Alamat,RT,RW,KelDesa,Kecamatan,KotaKabupaten,Provinsi,Agama,StatusPerkawinan,Pekerjaan,Kewarganegaraan):
                self.NIK = NIK
                self.Nama = Nama
                self.TempatLahir = TempatLahir
                self.TanggalLahir = TanggalLahir
                self.JenisKelamin = JenisKelamin
                self.GolonganDarah = GolonganDarah
                self.Alamat = Alamat
                self.RT = RT
                self.RW = RW
                self.KelDesa = KelDesa
                self.Kecamatan = Kecamatan
                self.KotaKabupaten = KotaKabupaten
                self.Provinsi = Provinsi
                self.Agama = Agama
                self.StatusPerkawinan = StatusPerkawinan
                self.Pekerjaan = Pekerjaan
                self.Kewarganegaraan = Kewarganegaraan

        NIK = int(input('NIK                                                            : '))
        digit = len(str(abs(NIK)))
        while digit != 16:
            print('NIK anda salah, silahkan masukkan kembali')
            NIK = int(input('NIK                                                            : '))
            digit = len(str(abs(NIK)))
        Nama = str(input('Nama                                                           : '))
        Nama = Nama.upper()
        TempatLahir = str(input('Tempat Lahir                                                   : '))
        TempatLahir = TempatLahir.upper()
        TanggalLahir = input('Tanggal Lahir (DD-MM-YYYY)                                     : ')
        while True:
            JenisKelamin = input('Jenis Kelamin (1.Laki-laki/2.Perempuan)                        : ')
            if JenisKelamin in ['L','l','Laki-laki','laki-laki','1']:
                JenisKelamin = "LAKI-LAKI"
                break
            elif JenisKelamin in ['P','p','Perempuan','perempuan','2']:
                JenisKelamin = "PEREMPUAN"
                break                                                                                                                                                                                                                                                                                                                                                                                                                                                       
            else:
                print('Jenis Kelamin salah, Silahkan masukkan kembali')
        while True:
            GolonganDarah = str(input('Golongan Darah (A/B/O/AB)                                      : '))
            if GolonganDarah in ['A', 'a']:
                GolonganDarah = 'A'
                break
            elif GolonganDarah in ['B','b']:
                GolonganDarah = 'B'
                break
            elif GolonganDarah in ['O','o']:
                GolonganDarah = 'O'
                break
            elif GolonganDarah in ['AB','Ab','aB','ab']:
                GolonganDarah = 'AB'
                break
            else:
                print('Golongan Darah salah, Silahkan masukkan kembali')
        Alamat = input('Alamat                                                         : ')
        Alamat = Alamat.upper()
        RT = input('RT                                                             : ')
        RW = input('RW                                                             : ')
        KelDesa = input('Kel/Desa                                                       : ')
        KelDesa = KelDesa.upper()
        Kecamatan = input('Kecamatan                                                      : ')
        Kecamatan = Kecamatan.upper()
        while True:
            KotaKabupaten = input('Kota/Kabupaten (1/2)                                           : ')
            if KotaKabupaten == '1':
                Kota = input('Nama Kota                                                      : ')
                KotaKabupaten = ('Kota '+Kota)
                break
            elif KotaKabupaten == '2':
                Kabupaten = input('Nama Kabupaten                                                 : ')
                KotaKabupaten = ('Kabupaten '+Kabupaten)
                break
            else:
                print('Pilihan anda salah, silahkan ketik 1 untuk kota dan ketik 2 untuk kabupaten')
        KotaKabupaten = KotaKabupaten.upper()
        Provinsi = input('Provinsi                                                       : ')
        Provinsi = Provinsi.upper()
        Agama = input('Agama (1.Islam/2.Kristen/3.Katholik/4.Hindu/5.Budha/6.Konghucu): ')
        while True:
            if Agama in ['ISLAM','Islam','islam','1']: 
                Agama = 'ISLAM'
                break
            elif Agama in ['KRISTEN','Kristen','kristen','2']:
                Agama = 'KRISTEN'
                break
            elif Agama in ['KATHOLIK','Katholik','katholik','3']:
                Agama = 'KATHOLIK'
                break
            elif Agama in ['HINDU','Hindu','hindu','4']:
                Agama = 'HINDU'
                break
            elif Agama in ['BUDHA','Budha','budha','5']:
                Agama = 'BUDHA'
                break
            elif Agama in ['KONGHUCU','Konghucu','konghucu','6']:
                Agama = 'KONGHUCU'
                break
            else:
                print('Agama anda salah, mohon masukkan kembali')
        StatusPerkawinan = input('Status Perkawinan (1.Kawin/2.Belum Kawin)                      : ')
        while True:
            if StatusPerkawinan in ['KAWIN','Kawin','kawin','1']:
                StatusPerkawinan = 'KAWIN'
                break
            elif StatusPerkawinan in ['BELUM KAWIN','Belum Kawin','Belum kawin','belum kawin','2']:
                StatusPerkawinan = 'BELUM KAWIN'
                break
            else:
                print('Status anda salah, mohon masukkan kembali')
        Pekerjaan = input('Pekerjaan                                                      : ')
        Pekerjaan = Pekerjaan.upper()
        Kewarganegaraan = input('Kewarganegaraan                                                : ')
        while True:
            if Kewarganegaraan in ['WNI','Wni','wni','INDONESIA','Indonesia','indonesia']:
                Kewarganegaraan = 'WNI'
                break
            else:
                Kewarganegaraan = 'WNA'
                break

        DataKTP = KTP(NIK,Nama,TempatLahir,TanggalLahir,JenisKelamin,GolonganDarah,Alamat,RT,RW,KelDesa,Kecamatan,KotaKabupaten,Provinsi,Agama,StatusPerkawinan,Pekerjaan,Kewarganegaraan)
        print()

        ulang = int(input('Apakah data yang dimasukkan sudah Benar ? Ketik 1 jika sudah benar dan 2 jika belum benar. \n'))
        if ulang == 1:
            ListKTP.append(DataKTP)
            print('')
            print(('Data Anda tersimpan sebagai KTP ' + str(len(ListKTP))))
            print('')
        else:
            continue

    elif choice == 2 :
        print()
        print('Anda memilih [2] Lihat Data KTP ')
        print()
        kartu_nomor = int(input('Pilih nomor KTP yang ingin dilihat : '))
        print('','\nKTP',kartu_nomor,'\n')

        print('{0}KTP {0}'.format(' '*33))
        print('{0}'.format('-'*70))
        print('|{0}|'.format(' '*68))
        provinsi='PROVINSI {}'.format(ListKTP[kartu_nomor -1].Provinsi)
        while True:
                if (int(len(provinsi))%2==1):
                        provinsi='{0} '.format(provinsi)
                        a=int((68-int(len(provinsi)))/2)
                        break
                else:                                
                        a=int((68-int(len(provinsi)))/2)
                        break
        print('|{0}{1}{0}|'.format(' '*a,provinsi))
        kota='{}'.format(ListKTP[kartu_nomor -1].KotaKabupaten.upper())
        while True:
                if (int(len(kota))%2==1):
                        kota='{0} '.format(kota)
                        a=int((68-int(len(kota)))/2)
                        break
                else:                                
                        a=int((68-int(len(kota)))/2)
                        break
        print('|{0}{1}{0}|'.format(' '*a,kota))  
        print('|{0}|'.format(' '*68))
        nik="|  NIK          : {0}".format(ListKTP[kartu_nomor -1].NIK)
        print("{0}{1}|".format(nik,' '*int(69-int(len(nik)))))
        print('|{0}------------  |'.format(' '*54))
        nama='|  Nama             :{0}'.format(ListKTP[kartu_nomor -1].Nama)
        print("{0}{1}|          |  |".format(nama,' '*int(55-int(len(nama)))))
        ttl='|  Tempat/Tgl Lahir :{0}, {1}'.format(ListKTP[kartu_nomor -1].TempatLahir,ListKTP[kartu_nomor -1].TanggalLahir)
        print("{0}{1}|          |  |".format(ttl,' '*int(55-int(len(ttl)))))
        jeniskelamin='|  Jenis kelamin    :{0}'.format(ListKTP[kartu_nomor -1].JenisKelamin)
        golongandarah='      Gol. Darah :{0}'.format(ListKTP[kartu_nomor -1].GolonganDarah)
        jekgol=int(len(jeniskelamin))+int(len(golongandarah))
        print('{0}{1}{2}|          |  |'.format(jeniskelamin,golongandarah,' '*int(55-int(jekgol))))
        alamat='|  Alamat           :{0}'.format(ListKTP[kartu_nomor -1].Alamat)
        print("{0}{1}|          |  |".format(alamat,' '*int(55-int(len(alamat)))))
        rtrw='|      RT/RW        :{0}/{1}'.format(ListKTP[kartu_nomor -1].RT,ListKTP[kartu_nomor -1].RW)
        print('{0}{1}|   FOTO   |  |'.format(rtrw,' '*int(55-int(len(rtrw)))))
        kelurahan="|      Kel/Desa     :{0}".format(ListKTP[kartu_nomor -1].KelDesa)
        print('{0}{1}|          |  |'.format(kelurahan,' '*int(55-int(len(kelurahan)))))
        kecamatan="|      Kecamatan    :{0}".format(ListKTP[kartu_nomor -1].Kecamatan)
        print('{0}{1}|          |  |'.format(kecamatan,' '*int(55-int(len(kecamatan))))) 
        agama="|  Agama            :{0}".format(ListKTP[kartu_nomor -1].Agama)
        print("{0}{1}|          |  |".format(agama,' '*int(55-int(len(agama)))))
        status="|  Status Perkawinan:{0}".format(ListKTP[kartu_nomor -1].StatusPerkawinan)
        print("{0}{1}------------  |".format(status,' '*int(55-int(len(status)))))
        pekerjaan="|  Pekerjaan        :{0}".format(ListKTP[kartu_nomor -1].Pekerjaan)
        while True:
                if (int(len(ListKTP[kartu_nomor -1].KotaKabupaten))%2==1):
                        namkot='{0} '.format(ListKTP[kartu_nomor -1].KotaKabupaten)
                        c=int((16-int(len(namkot)))/2)
                        break
                else:
                        c=int((16-int(len(ListKTP[kartu_nomor -1].KotaKabupaten)))/2)
                        break
        print("{0}{1}{2}{3}{2}|".format(pekerjaan,' '*int(53-int(len(pekerjaan))),' '*c,ListKTP[kartu_nomor -1].KotaKabupaten))
        kewarganegaraan="|  Kewarganegaraan  :{0}".format(ListKTP[kartu_nomor -1].Kewarganegaraan)
        print("{0}{1} {2}   |".format(kewarganegaraan,' '*int(55-int(len(kewarganegaraan))),hariini))
        masaberlaku="|  Masa Berlaku     :{0}".format("SEUMUR HIDUP")
        print("{0}{1}|".format(masaberlaku,' '*int(69-int(len(masaberlaku)))))
        print('|{0}TTD       |'.format(' '*58))
        print('|{0}|'.format(' '*68))
        print('-'*70)    
 
    elif choice == 3 :
        print()
        print('Anda memilih [3] Hapus Data KTP')
        print()
        kartu_nomor = int(input('Pilih nomor KTP yang ingin dihapus : '))
        del ListKTP[kartu_nomor - 1]
        print('Kartu dengan nomor ' + str(kartu_nomor) + 'telah dihapus', '\n')
            
    elif choice == 4 :
        print()
        print('Anda memilih [4] Selesai')
        print()
        print('Anda telah keluar dari PROGRAM KTP')
        print()
        print('>>>>>>>>>> TERIMA KASIH <<<<<<<<<<')
        break

    else :
        print()
        print('Pilihan anda salah, silahkan masukkan kembali')
        print()