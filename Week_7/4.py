def pajak(cls):
    def indonesia(self):
        print(f"Pajak penghasilan {self.nama} di indonesia adalah {self.bayar*11/100} rupiah\n")
    def jepang(self):
        print(f"Pajak penghasilan {self.nama} di jepang adalah {self.bayar*10/100} yen\n")
    def india(self):
        print(f"Pajak penghasilan {self.nama} di india adalah {self.bayar*39/100} rupee\n")
    cls.indonesia = indonesia
    cls.jepang = jepang
    cls.india = india
    return cls

@pajak
class penghasilan:
    def __init__(self,nama,bayar):
        self.bayar=bayar
        self.nama=nama

dono=penghasilan("dono",1300000)
dono.indonesia()
sitoshi=penghasilan("sitoshi",39000)
sitoshi.jepang()
sarukhan=penghasilan("sarukhan",290000)
sarukhan.india()

        