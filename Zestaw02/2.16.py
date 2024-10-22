def replace(line):
    new_line = line.replace("GvR","Guido van Rossum")
    return new_line
line = "Ala ma dwa koty zaprogramowane przez GvR ale także hipopotana ale marzy by miec rybe"
print(f"Input: {line},\n Output: {replace(line)}")