def sort_alfabetical(line):
    new_line = line.split()
    sorted_alphabetical = sorted(new_line)
    return ' '.join(sorted_alphabetical)

def sort_maxlen(line):
    new_line = line.split()
    sorted_maxlen = sorted(new_line, key=len, reverse=True)
    return ' '.join(sorted_maxlen)

line = "Ala ma dwa koty zaprogramowane przez gvR ale także hipopotana ale marzy by miec rybe"
print(f"Input: {line}\nPosortowana alfabetycznie: {sort_alfabetical(line)}\nPosortowana wzgledem dlugosci: {sort_maxlen(line)}")