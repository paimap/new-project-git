class Person:
    def __init__(self,nama:str,saldo:int):
        self.__nama = nama
        self.__saldo = saldo

    def cek_saldo(self):
        print(f"sisa saldo {self.__nama} adalah {self.__saldo}")

    def belanja(self, harga:int,barang:str):
        if harga<=self.__saldo:
            self.__saldo-=harga
            print(f"{self.__nama} belanja {barang} seharga {harga} ")
        else:
            print("saldo tidak cukup")

if __name__ == "__main__":
    budi = Person("Budi", 50000)
    budi.cek_saldo
    budi.belanja(20000,"baju")
    budi.cek_saldo()


        




