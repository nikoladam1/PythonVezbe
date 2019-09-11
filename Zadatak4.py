jan = 0.17
feb = 1.9
mar = 0.13
apr = 1.02
may = 0.78
jun = 0.67

july = 0.67
augu = 0.35
sept = 1.18
octo = 0.20
nov = 0.66
dec = 1

polaKoef = jan+feb+mar+apr+may+jun
print("Polugodisnji koeficijent = "+str(polaKoef))

koef = polaKoef + july +augu +sept +octo +nov+ dec
print("Godisnji koeficijent = "+str(koef))

osnovica = 40000
desOsn = osnovica / 10
print("Desetina osnovice = "+str(desOsn))

bonus = desOsn * koef
print("Bonus = "+str(bonus))
