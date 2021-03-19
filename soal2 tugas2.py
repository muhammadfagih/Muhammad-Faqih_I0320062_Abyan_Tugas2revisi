# biodata
nama = "Muhammad Faqih"
nim = "I0320062"
agama = "Islam"
jenis_kelamin = "Laki-laki"
prodi = "Teknik Industri"
angkatan = 2020
tempat_lahir = "Jakarta"
tgl_lahir = "13 Februari 2003"

# umur
tlahir = 13
blahir = 2
ylahir = 2003
lahir = tlahir+(blahir*30)+(ylahir*365)
tsekarang = 20
bsekarang = 3
ysekarang = 2021
sekarang = tsekarang+(bsekarang*30)+(ysekarang*365)
tahun = int((sekarang-lahir)/365)
bulan = int(((sekarang-lahir)%365)/30)
hari = int(((sekarang-lahir)%365)%30)

# alamat tempat tinggal
alamat = "Jl. Haji samali ujung Komp. LAN Pertambangan No. 43A"

# informasi tambahan
berat_badan = 60
tinggi_badan = 170
uk_sepatu = 42.5
us_sepatu = 9
makanan_favorit = "Ayam goreng"
minuman_favorit = "es teh manis"
cita_cita = "menjadi pengusaha sukses"
hobi = "Futsal, Basket, Bermain Game"

# tampilkan semua informasi di layar
print("Nama :",nama)
print("NIM  :",nim)
print("Agama :",agama)
print("Jenis kelamin :",jenis_kelamin)
print("Alamat :",alamat)
print("Saya adalah seorang mahasiswa",prodi,"angkatan",angkatan)
print("Saya lahir di",tempat_lahir,"pada",tgl_lahir,"dan sekarang berumur",tahun,"tahun",bulan,"bulan",hari,"hari")
print("Hobi saya adalah",hobi)
print("Berat badan saya",berat_badan,"kg, dan","tinggi saya",tinggi_badan,"cm")
print("Ukuran sepatu saya UK",uk_sepatu,"atau US",us_sepatu)
print("Makanan favorit saya",makanan_favorit,"ditemani dengan",minuman_favorit)
print("Cita-cita saya",cita_cita)