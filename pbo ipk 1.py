FILE_MAHASISWA = "data_mahasiswa.txt"
FILE_DOSEN     = "data_dosen.txt"
FILE_MATKUL    = "data_matkul.txt"
FILE_KRS       = "data_krs.txt"
FILE_PENILAIAN = "data_penilaian.txt"
FILE_KHS       = "data_khs.txt"


class Mahasiswa:
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        self.krs = []
        self.nilai = []
    def tambah_mahasiswa(self):
        return f"{self.npm}|{self.nama}"
    def tampil_mahasiswa(self):
        return f"{self.npm} - {self.nama}"
    def simpan_mahasiswa(mahasiswa_list):
    with open(FILE_MAHASISWA, "w") as f:
        for m in mahasiswa_list:
            f.write(f"{m.nim}|{m.get_nama()}\n")


class Dosen:
    def __init__(self, nama):
        self.nama = nama
        
    def tambah_dosen(self):
        return f"{self.nama}"

    def tampil_dosen(self):
        return f"Dosen: {self.nama}"


class MataKuliah:
    def __init__(self, nama_matkul, sks):
        self.nama_matkul = nama_matkul
        self.sks = sks

    def tambah_matkul(self):
        return f"{self.nama_matkul}|{self.sks}"

    def tampil_matkul(self):
        return f"{self.nama_matkul} ({self.sks} SKS)"
    def simpan_matkul(matkul_list):
    with open(FILE_MATKUL, "w") as f:
        for mk in matkul_list:
            f.write(f"{mk.nama}|{mk.sks}\n")

class Penilaian:
    def __init__(self, matkul, angka):
        self.matkul = matkul
        self.angka = angka
        self.huruf, self.bobot = self.konversi(angka)

    def konversi(self, angka):
        if angka >= 85: return "A", 4
        elif angka >= 70: return "B", 3
        elif angka >= 60: return "C", 2
        elif angka >= 50: return "D", 1
        else: return "E", 0
    def input_nilai(self, angka):
        self.angka = angka
        self.huruf, self.bobot = self.konversi(angka)
    def hitung_nilai(self):
        return self.bobot * self.matkul.sks
    def tampil_nilai(self):
        return f"{self.matkul.nama_matkul} | {self.angka} | {self.huruf}"
    def simpan_nilai(mahasiswa_list):
    with open(FILE_NILAI, "w") as f:
        for m in mahasiswa_list:
            for n in m.nilai:
                f.write(f"{m.nim}|{n.matkul.nama}|{n.angka}\n")

class KRS:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa

    def tampil_mahasiswa(self):
        return self.mahasiswa.tampil_mahasiswa()

    def tampil_matkul(self):
        return [mk.tampil_matkul() for mk in self.mahasiswa.krs]

    def tampil_krs(self):
        return f"KRS {self.mahasiswa.nama}:\n" + "\n".join(self.tampil_matkul())
def simpan_krs(mahasiswa_list):
    with open(FILE_KRS, "w") as f:
        for m in mahasiswa_list:
            for mk in m.krs:
                f.write(f"{m.nim}|{mk.nama}\n")

class KHS:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa

    def hitung_ipk(self):
        total_bobot = sum(n.hitung_nilai() for n in self.mahasiswa.nilai)
        total_sks = sum(n.matkul.sks for n in self.mahasiswa.nilai)
        return total_bobot / total_sks if total_sks else 0

    def tampil(self):
        hasil = [n.tampil_nilai() for n in self.mahasiswa.nilai]
        return f"KHS {self.mahasiswa.nama}:\n" + "\n".join(hasil) + f"\nIPK: {round(self.hitung_ipk(), 2)}"

    def simpan_semua(mahasiswa_list, matkul_list):
    simpan_mahasiswa(mahasiswa_list)
    simpan_matkul(matkul_list)
    simpan_krs(mahasiswa_list)
    simpan_nilai(mahasiswa_list)
    

