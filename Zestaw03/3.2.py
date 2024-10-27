L = [3, 5, 4] ; L = L.sort() # L w tym przypadku bedzie none, poniewaz .sort() jedynie modifykuje oryginalna liste, a sama zwraca None
x, y = 1, 2, 3 # Nie mozemy przypisywac 3 wartosci 2 zmiennym (brakuje dodatkowej zmiennej)
X = 1, 2, 3 ; X[1] = 4 # X to nie lista, tylko tuple'a dodatkowo w niej nie mozemy zmieniac przypisywanych wartosci
X = [1, 2, 3] ; X[3] = 4 # Ta lista ma tylko indeksy od 0 do 2, wiec przypisanie do indeksu 3 spowoduje blad
X = "abc" ; X.append("d") # funkcja .append() nie działa dla stringów
L = list(map(pow, range(8))) #funkcja pow() wymaga 2 argumentów pow(base,exp)