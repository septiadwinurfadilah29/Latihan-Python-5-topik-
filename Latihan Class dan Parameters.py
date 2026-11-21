class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo saya {self.nama}")

    def hello(self, nama):
        print(f"halo {nama} saya {self.nama}")


mahasiswa1 = Mahasiswa()
mahasiswa1.nama = "asep"
mahasiswa1.perkenalan()

mahasiswa2 = Mahasiswa()
mahasiswa2.nama = "tia"
mahasiswa2.hello("asep")