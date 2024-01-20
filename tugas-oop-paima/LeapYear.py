tahun = 2024

if tahun%400 == 0:   #jika tahun habis dibagi 400 maka merupakan tahun kabisat
    print("tahun kabisat")
elif tahun%100 == 0:   #jika tahun tidak habis dibagi 400 dan tahun habis dibagi 100 maka bukan tahun kabisat
    print("bukan tahun kabisat")
elif tahun%4 == 0: #jika tahun tidak habis dibagi 400, tahun tidak habis dibagi 100, dan tahun habis dibagi 4 maka merupakan tahun kabisat
    print("tahun kabisat")
else:  #jika tahun tidak habis dibagi 400, tahun tidak habis dibagi 100, dan tahun tidak habis dibagi 4,  maka bukan merupakan tahun kabisat
    print("bukan tahun kabisat")

    