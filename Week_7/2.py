class Person:
    sehat = False  

    def dinyatakan_sehat(self):
        self.sehat = True  

joni = Person()
eko = Person()

joni.dinyatakan_sehat()
print("Joni sehat: ", joni.sehat)  # Nilai Terbarui
print("Eko sehat: ", eko.sehat)  # Nilai Default