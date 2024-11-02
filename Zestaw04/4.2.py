def drawingMeasure(n):
    text = ""
    count = ""
    
    for int_num in range(n):
        text += "|...."
        if int_num < 10:
            count += f"{int_num}    "
        else:
            count += f"{int_num}   "

    text += "|"
    count += f"{n}   "  
    result = text + "\n" + count
    return result

def rectangle(rows,columns):
    x = (3 * columns) + 1  
    text = ""

    for i in range(rows):   
        text += "+---" * columns + "+\n"
        text += "|   " * columns + "|\n"
    text += "+---" * columns + "+\n"
    return text

print(drawingMeasure(11))
print(rectangle(4,4))