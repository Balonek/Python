import itertools    
import random

iterator_1 = itertools.cycle(range(0, 2))
for i in range(5):
    print(next(iterator_1)) 
print("\n")

list = ["N", "E", "S", "W"]
iterator_2 = (random.choice(list) for _ in itertools.count()) 
for i in range(8):
    print(next(iterator_2))
    
print("\n")
iterator_3 = itertools.cycle(range(0, 7))
for i in range(10):
    print(next(iterator_3)) 