def cube():
    while True:
        reply = input("Enter a number! (Type 'stop' to end the program)\n")
        if reply == "stop":
            break
        try:
            number = float(reply)
            print(f"The cube of the number {number} is: {pow(number, 3)}")
        except ValueError:
            print("Error, you didn't enter a number or 'stop' ")
cube()
