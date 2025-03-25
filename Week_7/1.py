class Passenger:
    TITLES = ("Mr", "Mrs", "Ms")  

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s bukan judul yang valid." % title)
        self.title = title  
        self.fname = fname  
        self.lname = lname  

# Pembuatan Objek
p1 = Passenger("Mr", "Kiewlamphone", "Souvanlith")

# Mengakses atribut kelas dari objek
print(p1.TITLES)

# Mengakses atribut kelas dari kelas
print(Passenger.TITLES)

# Mengakses atribut instance dari objek
print(p1.title)

# Percobaan mengakses atribut instance dari kelas 
print(Passenger.title)
