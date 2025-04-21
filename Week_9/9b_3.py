from collections import namedtuple

Orang = namedtuple("Orang", ["nama", "anak"])

def Class_decorator_tampilkan_info(cls):
    def tampilkan_info(self):
        print("Nama :", self.nama)
        print("Nama anak:")
        for i, anak in enumerate(self.anak, 1):
            print(f"{i}. {anak}")
    cls.tampilkan_info = tampilkan_info
    return cls

@Class_decorator_tampilkan_info
class Orang(Orang):
    pass

john = Orang("John Doe", ["Timmy", "Jimmy"])

john.anak.append("Tina")

john.tampilkan_info()

