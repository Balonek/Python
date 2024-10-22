def lista_i_3_bloki(L): 
    list = [str(num).zfill(3) for num in L] 
    result = ' '.join(list) 
    return result 
L = [42,515,5,3,6,30,235,351] 
print(f"Input: {L}\nOutput: {lista_i_3_bloki(L)}")