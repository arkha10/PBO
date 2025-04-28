from abc import ABC, abstractmethod
import random
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def __init__(self):
        self.damage = random.randint(10, 20)
    
    def attack(self):
        return f"Menebas musuh dengan pedang! Damage: {self.damage}"
class Bow(Weapon):
    def __init__(self):
        self.damage = random.randint(5, 15)
    
    def attack(self):
        return f"Menembakkan panah ke musuh! Damage: {self.damage}"
class Staff(Weapon):
    def __init__(self):
        self.damage = random.randint(15, 25)
    
    def attack(self):
        return f"Menghantam musuh dengan tongkat sihir! Damage: {self.damage}"
class WeaponFactory:
    @staticmethod
    def create_weapon(weapon_type):
        if weapon_type == "sword":
            return Sword()
        elif weapon_type == "bow":
            return Bow()
        elif weapon_type == "staff":
            return Staff()
        else:
            raise ValueError(f"Jenis senjata '{weapon_type}' tidak tersedia!")
print("=== PABRIK SENJATA FANTASY RPG ===")

pilihan_senjata = ["sword", "bow", "staff", "bow", "sword"]

for pilihan in pilihan_senjata:
    weapon = WeaponFactory.create_weapon(pilihan)
    print(weapon.attack())

