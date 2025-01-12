import random

"""(a) różne liczby int od 0 do n-1 w kolejności losowej,"""
def random_int_sequence(n):
    L = []
    for i in range(n):
        L.append(i)
    random.shuffle(L)
    return L

"""(b) różne liczby int od 0 do n-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),"""
def almost_sorted_from_random_int_sequence(n, swaps):
    L = []
    for i in range(n):
        L.append(i)
    for swap in range(swaps):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        L[i], L[j] = L[j], L[i]
    return L

"""(c) różne liczby int od 0 do n-1 prawie posortowane w odwrotnej kolejności,"""
def reversed_almost_sorted_from_random_int_sequence(n, swaps):

    L= [] 
    for i in range(n-1, -1, -1):
        L.append(i)
    for swap in range(swaps):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        L[i], L[j] = L[j], L[i]
    return L

""" (d) n liczb float w kolejności losowej o rozkładzie gaussowskim """ 
def gaussian_sequence(n, mu, sigma):
    return [random.gauss(mu, sigma) for i in range(n)]

""" (e)  n liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < n, np. k^2 = n).""" 
def repeated_values_sequence(n, k):
    if k >= n:
        raise ValueError("k musi być mniejsze od n")   
    L = []
    for i in range(n):
        random_number = random.randint(0, k-1)
        L.append(random_number)
    return L

if __name__ == "__main__":
    n = 10  
    k = 5   

    print("(a): " + str(random_int_sequence(n)))
    print("\n(b): " + str(almost_sorted_from_random_int_sequence(n, swaps=1)))
    print("\n(c): " + str(reversed_almost_sorted_from_random_int_sequence(n, swaps=1)))
    print("\n(d): " + str(gaussian_sequence(n, mu=0.0, sigma=1.0)))
    print("\n(e): " + str(repeated_values_sequence(n, k)))
