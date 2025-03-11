class barang:
    def __init__(self,merek,harga_satuan):
        self.merek=merek
        self.harga_satuan=harga_satuan #dalam ribu
    def __mul__(self,kuantitas):
            print('Banyaknya penjualan: ',kuantitas.qty_jual,'buah')
            return self.harga_satuan * kuantitas.qty_jual

class penjualan:
    def __init__(self,merek,qty_jua):
        self.merek=merek
        self.qty_jual=qty_jua



redmi10=barang("Redmi10",2140)
qty_maret=penjualan("redmi10",20)
print(f"Total penjualan {redmi10.merek} : {redmi10*qty_maret} ribu")
        