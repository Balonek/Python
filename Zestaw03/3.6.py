def rectangle():
    columns = int(input("Input number of columns: "))  
    rows = int(input("Input number of rows: "))  

    x = (3 * columns) + 1  
    text = ""

    for i in range(rows):
        text += "+---" * columns + "+\n"
        text += "|   " * columns + "|\n"
    text += "+---" * columns + "+\n"
    return print(f"Your rectangle:\n{text}")
rectangle()
        