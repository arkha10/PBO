from abc import ABC, abstractmethod
class gaji(ABC):
    def __init__(self, name, gaji):
        self.name = name
        self.gaji = gaji
    @abstractmethod
    def pokok(self):
        pass
    @abstractmethod
    def tunjangan(self):
        pass
class karyawan_tetap(gaji):
    def pokok(self):
        print(f"gaji pokok {self.name} sebagai pegawai tetap adalah {self.gaji} Juta")
    def tunjangan(self):
        print(f"tunjangan {self.name} sebagai pegawai tetap adalah {self.gaji*0.8} Juta")
    
class karyawan_magang(gaji):
    def pokok(self):
        print(f"gaji pokok {self.name} sebagai pegawai magang adalah {self.gaji*0.8} Juta")
    def tunjangan(self):
        print(f"tunjangan {self.name} sebagai pegawai magang adalah {self.gaji*0.6} Juta")

herman=karyawan_tetap("herman",20)
herman.pokok()
herman.tunjangan()
print("\n")
budi=karyawan_magang("budi",10)
budi.pokok()
budi.tunjangan()

