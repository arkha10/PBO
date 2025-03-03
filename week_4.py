class orang:  #soal nomor 1
    def __init__(self, depan, belakang,id):
        self.nama_depan=depan
        self.nama_belakang=belakang
        self.nomor_id=id

class mahasiswa(orang): #soal nomor 2
    SARJANA, MASTER,DOKTOR=range(3)
    def __init__(self,jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang=jenjang
        self.matkul= []
    
    def enrol(self,pelajaran):
        self.matkul.append(pelajaran)

class karyawan(orang):  #soal nomor 3
    TETAP,TDK_TETAP=range(2)
    def __init__(self,status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_karyawan=status

class dosen(karyawan):  #soal nomor 4
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar=[]
    def mengajar(self,matkul):
        self.matkul_diajar.append(matkul)

bowo=mahasiswa(mahasiswa.SARJANA,"bowo","nugroho",987654)  #soal nomor 5
bowo.enrol("basis data")

rizki=dosen(karyawan.TETAP,"rizki","setiabudi",456789)  #soal nomor 6
rizki.mengajar("statistik")


class pelajar:  #soal nomor 7
    def __init__(self):
        self.matkul=[]
    def enrol(self,blajar):
        self.matkul.append(blajar)

class pengajar:  #soal nomor 8
    def __init__(self):
        self.matkul_diajar=[]
    def mengajar(self,ajar):
        self.matkul_diajar.append(ajar)
        
class Asdos(orang, pelajar, pengajar):  #soal nomor 9
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pelajar.__init__(self)
        pengajar.__init__(self)

Asdos1=Asdos("uswatun", "hasanah", "456456")  #soal nomor 10
Asdos1.enrol("big data")
Asdos1.mengajar("kecerdasan buatan")

        