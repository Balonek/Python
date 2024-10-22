def liczenie(line):
    line = line.split()
    wynik = sum(len(wyraz) for wyraz in line)
    return wynik

# przykladowy input 
line = "\tAla  ma\ndwa\t\tkoty ale także ma dwa psy " # 28 znakow bez bialych znakow
print(f"""Input(line): {line}\n 
Output(Laczna długosc wyrazow w line): {liczenie(line)}""")