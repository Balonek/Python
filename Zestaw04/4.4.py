def fibonnaci(n):
        list = []
        if n==0: 
            return 0
        elif n==1: 
            return 1
        else:
            list.append(0)
            list.append(1) 
            for x in range(2,n+1):
                suma2 = list[x-1] + list[x-2]
                list.append(suma2)
        return list[n]

assert fibonnaci(0) == 0  
assert fibonnaci(1) == 1  
assert fibonnaci(2) == 1
assert fibonnaci(10) == 55
assert fibonnaci(14) == 377