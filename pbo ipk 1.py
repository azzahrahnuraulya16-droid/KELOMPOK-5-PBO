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
            f.write(f"{m.npm}|{m.nama}\n")
            
def load_mahasiswa():
    mahasiswa_list = []
    try:
        with open(FILE_MAHASISWA, "r") as f:
            for line in f:
                npm, nama = line.strip().split("|")
                mahasiswa_list.append(mahasiswa_list(npm, nama))
    except FileNotFoundError:
        pass
    return mahasiswa_list

class Dosen:
    def __init__(self, nama):
        self.nama = nama
        
    def tambah_dosen(self):
        return f"{self.nama}"

    def tampil_dosen(self):
        return f"Dosen: {self.nama}"

def simpan_dosen(dosen_list):
    with open(FILE_DOSEN, "w") as f:
        for d in dosen_list:
            f.write(f"{d.nama}\n")

def load_dosen():
    dosen_list = []
    try:
        with open(FILE_DOSEN, "r") as f:
            for line in f:
                nama = line.strip()
                dosen_list.append(dosen_list(nama))
    except FileNotFoundError:
        pass
    return dosen_list


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
            f.write(f"{mk.nama_matkul}|{mk.sks}\n")

def load_matkul():
    matkul_list = []
    try:
        with open(FILE_MATKUL, "r") as f:
            for line in f:
                nama, sks = line.strip().split("|")
                matkul_list.append(matkul_list(nama, int(sks)))
    except FileNotFoundError:
        pass
    return matkul_list


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

def load_nilai(mahasiswa_list):
    try:
        with open(FILE_NILAI, "r") as f:
            for line in f:
                npm, nama_mk, angka = line.strip().split("|")
                angka = int(angka)
                for m in mahasiswa_list:
                    if m.npm == npm:
                        for mk in m.krs:
                            if mk.nama_matkul == nama_mk:
                                m.nilai.append(Penilaian(mk, angka))
                                break
                        break
    except FileNotFoundError:
        pass


class KRS:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa

    def tampil_mahasiswa(self):
        return self.mahasiswa.tampil_mahasiswa()

    def tampil_matkul(self):
        return [mk.tampil_matkul() for mk in self.mahasiswa.krs]

    def tampil_krs(self):
        return f"KRS {self.mahasiswa.nama}:\n" + "\n".join(self.tampil_matkul())

def load_krs(mahasiwa_list,matkul_list):
    try:
        with open(FILE_KRS, "r") as af:
            for line f:
                npm,nama_mk, sks = line.strip().split("|")
                for m in mahasiswa_list:
                    if m.npm == npm:
                        for mk in matkul_list:
                            mk.nama_matkul == nama_mk:
                            m.krs.append(mk)
                            break
                        break 
    except FileNotFoundError:
        pass


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

