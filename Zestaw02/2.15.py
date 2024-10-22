def ciag(L):
    str_ciag =(str(liczba) for liczba in L)
    wynik = "".join(str_ciag)
    return wynik

L = [12,124,1,24,3]
print(f"Input: {L},\nOutput: {ciag(L)}")