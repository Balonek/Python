def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item,(list,tuple)):
                result.extend(flatten(item))
        elif isinstance(item,(int,float)):
            result.append(item)
    return result

seq1 = [1,(2,3),[],[4,(5,6,7)],8,[9]]
seq2 =  [1,(2,[3,(4,5)])]

assert flatten(seq1) == [1,2,3,4,5,6,7,8,9]
assert flatten(seq2) == [1,2,3,4,5]