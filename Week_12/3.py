import tkinter as tk
import random

class MathGame:
    def __init__(self, master):
        self.master = master
        master.title("Game Operasi Matematika")

        self.angka1 = 0
        self.angka2 = 0
        self.operasi = ""
        self.jawaban_benar = 0

        self.label_soal = tk.Label(master, text="", font=("Arial", 20))
        self.label_soal.pack(pady=10)

        self.entry_jawaban = tk.Entry(master, font=("Arial", 16))
        self.entry_jawaban.pack(pady=5)
        self.entry_jawaban.bind("<Return>", self.cek_jawaban) 

        self.button_jawab = tk.Button(master, text="Jawab", command=self.cek_jawaban, font=("Arial", 14))
        self.button_jawab.pack(pady=5)

        self.label_hasil = tk.Label(master, text="", font=("Arial", 16, "bold"))
        self.label_hasil.pack(pady=10)

        self.skor = 0
        self.label_skor = tk.Label(master, text=f"Skor: {self.skor}", font=("Arial", 12))
        self.label_skor.pack()

        self.buat_soal()

    def buat_soal(self):
        self.angka1 = random.randint(1, 10)
        self.angka2 = random.randint(1, 10)
        opsi = ["+", "-", "*", "/"]
        self.operasi = random.choice(opsi)

        if self.operasi == "+":
            self.jawaban_benar = self.angka1 + self.angka2
        elif self.operasi == "-":
            if self.angka1 < self.angka2:
                self.angka1, self.angka2 = self.angka2, self.angka1
            self.jawaban_benar = self.angka1 - self.angka2
        elif self.operasi == "*":
            self.jawaban_benar = self.angka1 * self.angka2
        elif self.operasi == "/":
            self.angka1 = self.angka2 * random.randint(1, 10) if self.angka2 != 0 else random.randint(1, 10)
            self.jawaban_benar = self.angka1 / self.angka2 if self.angka2 != 0 else 0

        self.label_soal.config(text=f"{self.angka1} {self.operasi} {self.angka2} = ?")
        self.entry_jawaban.delete(0, tk.END)
        self.label_hasil.config(text="")
        self.entry_jawaban.focus_set() 

    def cek_jawaban(self):
        try:
            jawaban_pengguna = int(float(self.entry_jawaban.get()))
            jawaban_benar_int = int(self.jawaban_benar)

            if jawaban_pengguna == jawaban_benar_int:
                self.label_hasil.config(text="Benar!", fg="green")
                self.skor += 1
            else:
                self.label_hasil.config(text=f"Salah. Jawaban yang benar adalah {jawaban_benar_int}", fg="red")
                self.skor -= 1

            self.label_skor.config(text=f"Skor: {self.skor}")
            self.master.after(1500, self.buat_soal)

        except ValueError:
            self.label_hasil.config(text="Masukkan angka!", fg="orange")
            self.entry_jawaban.focus_set()


root = tk.Tk()
game = MathGame(root)
root.mainloop()