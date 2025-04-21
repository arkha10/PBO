from collections import namedtuple
Koordinat = namedtuple('a', ['x','y'])
titik1 = Koordinat('2','4')
print("indeks :", titik1[0])
print("filed name :", titik1.x)
print("getattr :", getattr(titik1, "y"))
print(type(titik1))