class Pengunjung:
  def __init__(self):
    self.nama = ""

  def tanya_nama(self):
    print(f" {self.nama}: Eh btw, nama kamu siapa?")

  def jawab_dan_tanya_balik(self):
    print(f" {self.nama}: Namaku {self.nama}. Kalau kamu, namanya siapa?")

  def salam_kenal_septi(self):
    print(f" {self.nama}: Nama aku Septi, salam kenal!")

  def salam_kenal_aeryn(self):
    print(f" {self.nama}: Salam kenal juga yah!")


# Pengunjung 1 = Septi
pengunjung1 = Pengunjung()
pengunjung1.nama = "Septi"

# Pengunjung 2 = Aeryn
pengunjung2 = Pengunjung()
pengunjung2.nama = "Aeryn"

print("=== KEJADIAN TAK TERDUGA DI MUSEUM NASIONAL INDONESIA ===")
print(
    f" {pengunjung1.nama}: Permisi, aku boleh minta tolong fotoin aku di depan"
    " artefak ini tidak?"
)
print(
    f" {pengunjung2.nama}: Oh boleh banget! Sini kamera HP-nya... 1, 2, 3..."
    " Nah, ini hasilnya."
)
print(
    f" {pengunjung1.nama}: Wah hasilnya bagus dan pas banget! Terima kasih"
    " banyak ya."
)
print(f" {pengunjung2.nama}: Sama-sama.")

print("\n== PERKENALAN DI MUSEUM NASIONAL INDONESIA ==")
pengunjung1.tanya_nama()  # Septi tanya nama Aeryn
pengunjung2.jawab_dan_tanya_balik()  # Aeryn jawab Aeryn lalu tanya balik
pengunjung1.salam_kenal_septi()  # Septi: Nama aku Septi, salam kenal!
pengunjung2.salam_kenal_aeryn()  # Aeryn: Salam kenal juga yah!

print("\n=== OBROLAN DI MUSEUM NASIONAL INDONESIA ===")
print(f" {pengunjung1.nama}: Oh iya Aeryn, kamu lagi melihat-melihat apa tuh?")
print(
    f" {pengunjung2.nama}: Aku lagi memperhatikan artefak bersejarah yang"
    " berasal dari Kalimantan ini."
)
print(f" {pengunjung1.nama}: Wah artefaknya bagus yah!")
print(
    f" {pengunjung2.nama}: Iya, aku sangat kagum melihat peninggalan masa"
    " lalu yang masih terawat baik."
)
print(
    f" {pengunjung1.nama}: Kamu mau ikut bersama ku tidak melihat galeri"
    " lukisan di lantai dua?"
)
print(
    f" {pengunjung2.nama}: Wah boleh banget tuh, ayo kita keliling lihat koleksi"
    " lainnya bersama!"
)
print(
    f" {pengunjung1.nama}: Jangan lupa baca aturan museum ya, tidak boleh"
    " memotret menggunakan kilat."
)
print(
    f" {pengunjung2.nama}: Iya Septi, terima kasih sudah mengingatkanku."
)