makingDictionaryGlobal = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
def makingDictionary():
    return {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
def makingDictionaryFromTuples():
    return dict([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000)
    ])
def makingDictionary2():
    rom = "IVXLCDM"
    arabic_int = [1, 5, 10, 50, 100, 500, 1000]
    return {rom[i]: arabic_int[i] for i in range(len(rom))}

def roman2int(rom):
    roman_to_arabic = makingDictionaryGlobal  
    total = 0
    prev_value = 0

    for char in reversed(rom):
        value = roman_to_arabic.get(char)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


result = roman2int("MMMCDXLIX")
print(f"{result}")  # output: 3449
