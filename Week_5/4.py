class tahun:
    def __init__(self,tahun):
        self.tahun_lahir=tahun
    def __eq__(self, lain):
        return self.tahun_lahir != lain.tahun_lahir 
class tahun2(tahun):
    def __init__(self, tahun):
        super().__init__(tahun)
        self.tahun_lahir=tahun

andre=tahun(1919)
azriel=tahun2(1919)

if andre==azriel:
    print("tahun lahir berbeda")
else:
    print("tahun lahir sama")
    

