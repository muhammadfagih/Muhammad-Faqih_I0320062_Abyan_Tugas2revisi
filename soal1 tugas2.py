#luas persegi panjang
print("===== Menghitung Luas Persegi Panjang =====")
panjang = float(input("Masukkan panjang :"))
lebar = float(input("Masukkan lebar :"))
luas = (panjang*lebar)
print("Luas persegi panjang adalah",luas,"satuan")

#luas lingkaran
print("===== Menghitung Luas Lingkaran =====")
phi = 3.14
jari2 = float(input("Masukkan jari-jari :"))
luas = jari2*jari2*phi
print("Luas lingkaran adalah",luas,"satuan")

#luas kubus
print("===== Menghitung Luas Kubus =====")
sisi = float(input("Masukkan sisi :"))
luas_permukaan = 6*sisi*sisi
print("Luas permukaan kubus adalah",luas_permukaan,"satuan")

#celcius ke fahrenheit
print("===== Menghitung Konversi Suhu dari Celcius ke Fahrenheit")
celcius = float(input("Masukkan suhu celcius :"))
konversi = (((9/5)*celcius)+32)
print("Konversi suhu dari celcius ke fahrenheit adalah",konversi,"derajat")

#reamur ke kelvin
print("===== Menghitung konversi suhu dari Reamur ke Kelvin =====")
reamur = float(input("Masukkan suhu reamur :"))
konversi = ((5/4)*reamur)+273
print("Konversi suhu dari reamur ke kelvin adalah",konversi,"derajat")