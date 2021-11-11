ka = float(input("masukan alas atap: "))
ra = float(input("masukan tinggi atap: "))
ta = float(input("masukan tinggi tembok: "))

luas = 0.5 * (ka * ra)
persegi = ta * ta

print("rumah tersebut membutuhakan" ,str((luas + persegi ) / 5), "sak semen")