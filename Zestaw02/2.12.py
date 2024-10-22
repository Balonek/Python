def pierwszy_znak(line):
    new_line = line.split()
    wynik1 = ""
    for wyraz in new_line:
        wynik1 += wyraz[0] 
    return wynik1

def ostatni_znak(line):
    new_line = line.split()
    wynik2 = ""
    for wyraz in new_line:
        wynik2 += wyraz[-1] 
    return wynik2
line = "Ala ma dwa koty ale także ma dwa psy"

print(f"""Input:{line}\n
Napis z pierwszy znaków: {pierwszy_znak(line)}\n 
Napis z ostatnich znaków: {ostatni_znak(line)}\n""")