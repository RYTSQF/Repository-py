from matematika import persegi, lingkaran
from matematika.bangun_ruang import kubus, bola

sisi = 5
r = 7


print("Luas Persegi:", persegi.luas_persegi(sisi))
print("Keliling Persegi:", persegi.keliling_persegi(sisi))
print()


print("Luas Lingkaran:", round(lingkaran.luas_lingkaran(r), 2))
print("Keliling Lingkaran:", round(lingkaran.keliling_lingkaran(r), 2))
print()


print("Volume Kubus:", kubus.volume_kubus(sisi))
print("Luas Permukaan Kubus:", kubus.luas_permukaan_kubus(sisi))
print()


print("Volume Bola:", round(bola.volume_bola(r), 2))
print("Luas Permukaan Bola:", round(bola.luas_permukaan_bola(r), 2))
