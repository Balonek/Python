def drawingMeasure(size):
    text = ""
    count = ""
    
    for int_num in range(size):
        text += "|...."
        if int_num < 10:
            count += f"{int_num}    "
        else:
            count += f"{int_num}   "

    text += "|"
    count += f"{size}   "  
    result = text + "\n" + count
    return result

size = input("Input length of measure: ")
size = int(size)
result = drawingMeasure(size)
print(result)
