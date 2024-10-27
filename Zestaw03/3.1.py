x = 2; y = 3; 
if (x > y): 
    result = x; # bez średnika 
else:
    result = y; # bez średnika 
for i in "axby": if ord(i) < 100: print (i) # if musi mieć wcięcia z boku, oraz w tym przypadku znajdowac sie pod petla for
for i in "axby": print (ord(i) if ord(i) < 100 else i) # składnia poprawna
