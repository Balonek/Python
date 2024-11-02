def zmiana_iteracyjna(L,left,right):
    while left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left+=1
        right-=1
    return L
def zmiana_rekurencyjna(L,left,right):
    if left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        zmiana_rekurencyjna(L,left+1,right-1)
    return L
L = [1,2,3,4,5,6,7,8]

assert zmiana_iteracyjna(L[:],2,4) == [1,2,5,4,3,6,7,8]
assert zmiana_iteracyjna(L[:],3,3) == [1,2,3,4,5,6,7,8]
assert zmiana_iteracyjna(L[:],1,5) == [1,6,5,4,3,2,7,8]

assert zmiana_rekurencyjna(L[:],2,4) == [1,2,5,4,3,6,7,8]
assert zmiana_rekurencyjna(L[:],3,3) == [1,2,3,4,5,6,7,8]
assert zmiana_rekurencyjna(L[:],1,5) == [1,6,5,4,3,2,7,8]
