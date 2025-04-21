class MLM:
    jumlah_anggota=0
    def __init__(self, depan, belakang):
        self.depan = depan
        self.belakang = belakang
        self.nomor=MLM.jumlah_anggota
        MLM.jumlah_anggota+=1

    @property
    def nama_lenkap(self):
        return print(self.depan,self.belakang,"adalah anggota ke ",self.nomor)

    @classmethod
    def cek_jumlah_anggota(cls, a): 
        if MLM.jumlah_anggota<a:
            print(f"jumlah anggota MLM ini kurang dari {a}")
        elif MLM.jumlah_anggota>a:
            print(f"jumlah anggota MLM ini lebih dari {a}")
        else:
            print(f"jumlah anggota MLM ini adalah {a}")

    
    @staticmethod
    def Potensi_cuan(Modal):
        return print("jika modalmu {}, maka keuntunganmu {}".format(Modal,Modal*6))
    
arsa = MLM("arsa","saleh")
mizan=MLM("Mizan","ahmad")
harun=MLM("rizki","harun")
anhar=MLM("anharun","mudi")

harun.nama_lenkap
MLM.cek_jumlah_anggota(6)
MLM.Potensi_cuan(600)





