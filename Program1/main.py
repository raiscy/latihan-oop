class Mahasiswa:
    def __init__(self, nama, nim, jurusan, tahun_masuk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.tahun_masuk = tahun_masuk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Tahun Masuk: {self.tahun_masuk}")

class InputForm:
    @staticmethod
    def input_data_mahasiswa():
        print("=== Form Input Data Mahasiswa ===")
        
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        jurusan = input("Masukkan Jurusan: ")
        
        while True:
            tahun_masuk = input("Masukkan Tahun Masuk (YYYY): ")
            if tahun_masuk.isdigit() and len(tahun_masuk) == 4:
                break
            else:
                print("Tahun masuk tidak valid. Harap masukkan tahun dalam format YYYY.")

        return Mahasiswa(nama, nim, jurusan, tahun_masuk)

class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self):
        mahasiswa = InputForm.input_data_mahasiswa()
        self.daftar_mahasiswa.append(mahasiswa)
        print("Data mahasiswa berhasil ditambahkan.")

    def tampilkan_semua_mahasiswa(self):
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        print("\n=== Informasi Semua Mahasiswa ===")
        for mhs in self.daftar_mahasiswa:
            mhs.tampilkan_info()
            print()  # Untuk memberi jarak antar mahasiswa

    def cari_mahasiswa(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                print("\n=== Data Mahasiswa Ditemukan ===")
                mhs.tampilkan_info()
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

    def hapus_mahasiswa(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                self.daftar_mahasiswa.remove(mhs)
                print("Data mahasiswa berhasil dihapus.")
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

    def ubah_mahasiswa(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                print("=== Form Ubah Data Mahasiswa ===")
                mhs.nama = input("Masukkan Nama Baru: ")
                mhs.jurusan = input("Masukkan Jurusan Baru: ")
                
                while True:
                    tahun_masuk = input("Masukkan Tahun Masuk Baru (YYYY): ")
                    if tahun_masuk.isdigit() and len(tahun_masuk) == 4:
                        mhs.tahun_masuk = tahun_masuk
                        break
                    else:
                        print("Tahun masuk tidak valid. Harap masukkan tahun dalam format YYYY.")
                
                print("Data mahasiswa berhasil diubah.")
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

def menu_data(data_mahasiswa):
    while True:
        print("\n=== Menu Data ===")
        print("1. Tambah Mahasiswa")
        print("2. Ubah Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            data_mahasiswa.tambah_mahasiswa()
        elif pilihan == '2':
            nim = input("Masukkan NIM yang akan diubah: ")
            data_mahasiswa.ubah_mahasiswa(nim)
        elif pilihan == '3':
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_view(data_mahasiswa):
    while True:
        print("\n=== Menu View ===")
        print("1. Tampilkan Semua Mahasiswa")
        print("2. Cari Mahasiswa")
        print("3. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            data_mahasiswa.tampilkan_semua_mahasiswa()
        elif pilihan == '2':
            nim = input("Masukkan NIM yang dicari: ")
            data_mahasiswa