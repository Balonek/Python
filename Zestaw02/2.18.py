def numers_of_0(number):
    new_number = str(number)
    result = new_number.count("0")
    return result
number = 2000222222222220002222
print(f"Input: {number},\nOutput: Liczba 'zer' w liczbie: {numers_of_0(number)}")