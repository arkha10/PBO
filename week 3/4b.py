class koordinat2d:
    x=0
    y=0

    def __init__(self,x,y):
        self.x=x
        self.y=y

class koordinat3d(koordinat2d):
    z=0

    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    
    def tampilkan_koor(self):
        print("x = ",self.x)
        print("y = ",self.y)
        print("z = ",self.z)
titik1 = koordinat3d(1,2,3)
titik1.tampilkan_koor()
delattr(titik1,"z")
print("efek fungsi delattr()")
titik1.tampilkan_koor()

del titik1.y
print("efek keyword del")
titik1.tampilkan_koor()