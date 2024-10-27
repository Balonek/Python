def finding(x, y):
    match (x, y):
        case (int(),int()):
            new_x, new_y = set(str(x)), set(str(y))
        case (str(), str()):
            new_x, new_y = set(x), set(y)
        case _:
            raise ValueError("Error, not enter number or str")
    common_elements = list(new_x & new_y)
    all_elements = list(new_x | new_y)
    return common_elements, all_elements

num1, num2 = 2402, 3502
common_elements, all_elements = finding(num1, num2)

print("For numbers:")
print("Common elements:", common_elements)
print("All unique elements:", all_elements)

str1, str2 = "abcdef", "defgbhi"
common_elements, all_elements = finding(str1, str2)

print("\nFor strings:")
print("Common elements:", common_elements)
print("All unique elements:", all_elements)