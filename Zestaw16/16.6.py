import unittest

def swap(L, left, right):
    item = L[left]
    L[left] = L[right]
    L[right] = item
    
def iterative_quicksort(L):
    stack = [(0, len(L) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        mid = (left + right) // 2
        swap(L, left, mid)

        pivot = left
        for i in range(left + 1, right + 1):
            if L[i] < L[left]:
                pivot += 1
                swap(L, pivot, i)

        swap(L, left, pivot)

        stack.append((left, pivot - 1))
        stack.append((pivot + 1, right))  
        
class Tests(unittest.TestCase):    
    def test1(self):
        L = [3, 7, 8, 15, 2, 2, 1, 151]
        iterative_quicksort(L)
        self.assertEqual(L, [1, 2, 2, 3, 7, 8, 15, 151], "Blad")
    def test2(self):    
        L1 = [312, 41, 0, 2, 6, 13, 32]
        iterative_quicksort(L1)
        self.assertEqual(L1, [0, 2, 6, 13, 32, 41, 312], "Błąd")
    def test3(self):
        L2 = [0, 22222, -1, -3]
        iterative_quicksort(L2)    
        self.assertEqual(L2, [-3, -1, 0, 22222], "Błąd")
        
if __name__ == "__main__":
    unittest.main()
    