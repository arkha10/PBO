class Budi:
    def jabatan(self):
        print("Kakek")
class Lilia(Budi):
    def jabatan(self):
        print("Ibu")
class James(Lilia):
    def jabatan(self):
        print("Aku")
budi=Budi().jabatan()
lilia=Lilia().jabatan()
james=James().jabatan()