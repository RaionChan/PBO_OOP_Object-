class Mahasiswa:
  
  def __init__(self, nama, nim, jurusan, alamat):
    self.nama = nama
    self.nim = nim
    self.jurusan = jurusan
    self.alamat = alamat

  def ambilmatkul(self, matkul):
    self.matkul = matkul

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"NIM: {self.nim}")
    print(f"Jurusan: {self.jurusan}")
    print(f"Alamat: {self.alamat.tampilkan_info()}") 
    print(f"Mata Kuliah: {self.matkul.nama}")

class Dosen:

  def __init__(self, nama, nip, jurusan, matkul):
    self.nama = nama
    self.nip = nip
    self.jurusan = jurusan
    self.matkul = matkul

  def mengajar(self, mahasiswa):
    print(f"{self.nama} mengajar mata kuliah {self.matkul.nama} kepada {mahasiswa.nama}")

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"NIP: {self.nip}")
    print(f"Jurusan: {self.jurusan}")
    print(f"Mata Kuliah: {self.matkul.nama}") 

class Matkul:

  def __init__(self, nama, kode, sks):
    self.nama = nama
    self.kode = kode
    self.sks = sks

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Kode: {self.kode}")
    print(f"SKS: {self.sks}")

class Alamat:

  def __init__(self, jalan, kota, provinsi):
    self.jalan = jalan
    self.kota = kota
    self.provinsi = provinsi

  def tampilkan_info(self):
    return f"{self.jalan}, {self.kota}, {self.provinsi}" 

class Universitas:

  def __init__(self, nama):
    self.nama = nama
    self.mahasiswa = []
    self.dosen = []

  def daftarkan_mahasiswa(self, mahasiswa):
    self.mahasiswa.append(mahasiswa)

  def daftarkan_dosen(self, dosen):
    self.dosen.append(dosen)

  def tampilkan_mahasiswa(self):
    for mahasiswa in self.mahasiswa:
      mahasiswa.tampilkan_info()

  def tampilkan_dosen(self):
    for dosen in self.dosen:
      dosen.tampilkan_info()


mahasiswa1 = Mahasiswa("Caca", "035", "Teknik Informatika", Alamat("Jl. M. Said", "Bandar Lampung", "Lampung"))
mahasiswa2 = Mahasiswa("Ajeng", "031", "Teknik Informatika", Alamat("Jl. Telukkk", "Bandar Lampung", "Lampung"))
mahasiswa3 = Mahasiswa("Fira", "127", "Teknik Informatika", Alamat("Jl. Ikan Baung", "Bandar Lampung", "Lampung"))

matkul1 = Matkul("Pemrograman Berbasis Objek", "IF123", 3)
matkul2 = Matkul("Algoritma dan Pemrograman", "IF124", 4)

dosen1 = Dosen("Pak Puput", "12", "Teknik Informatika", matkul1)
dosen2 = Dosen("Pak Xavier", "13", "Teknik Informatika", matkul2)

mahasiswa1.ambilmatkul(matkul1)  
mahasiswa2.ambilmatkul(matkul2)  
mahasiswa3.ambilmatkul(matkul1) 

dosen1.mengajar(mahasiswa1)
dosen2.mengajar(mahasiswa2)


print ("")
print ("Daftar Mahasiswa")
print ("================")
print ("")
mahasiswa1.tampilkan_info()
print ("")
mahasiswa2.tampilkan_info()
print ("")
mahasiswa3.tampilkan_info()

print ('Dosen')
print ('================')
print ('')
dosen1.tampilkan_info()
dosen2.tampilkan_info()






