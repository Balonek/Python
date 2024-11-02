def sum_seq(squence):
    result = []
    for item in squence:
        if isinstance(item,(list,tuple)):
                result.append(sum_seq(item))
        elif isinstance(item,(int,float)):
            result.append(item)
    x = sum(result)
    return x

seq1 = [1,(2,3),[],[4,(5,6,7)],8,[9]]
seq2 =  [1,(2,[3,(4,5)])]

assert sum_seq(seq1) == 45
assert sum_seq(seq2) == 15