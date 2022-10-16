def myDay():
    x = int(input("masukan umur dalam hari : "))
    
    sisa = x % 365
    if x >= 365:
        tahun = x // 365
        print(f"{tahun} tahun")

    if x >= 30:
        bulan = sisa // 30
        sisa_hari = sisa % 30
        print(f"{bulan} bulan")

    if x >= 0:
        hari = sisa_hari
        print(f"{hari} hari")

myDay()

 