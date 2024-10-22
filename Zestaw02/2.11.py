def dodawanie_(slowo):
    for znak in slowo:
        lista.append(znak + "_")
    return ''.join(lista)[:-1]
    
slowo = "word"
lista = []
print(f"Input: 'word', Output: {dodawanie_(slowo)}")