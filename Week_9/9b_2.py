from collections import namedtuple
Orang = namedtuple("Orang", "nama anak")
john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))
