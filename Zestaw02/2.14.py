def najdlusze_slowo(line):
    new_line = line.split()
    sorted_words = sorted(new_line, key=len, reverse=True)
    return sorted_words[0]

line = "\tAla  ma\ndwa\t\tkoty ale także hipopotana ale marzy by miec rybe"
the_longest_word = najdlusze_slowo(line)
size_of_the_longest_word = len(the_longest_word)

print(f"Input: {line}\nOutput: Najdłusze słowo: {the_longest_word} ,a jego długość wynosi {size_of_the_longest_word}")