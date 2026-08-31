def value(colors):
    values = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    resistor_value = ""
    for index in range(0, 2):
        for number, color in enumerate(values):
            if colors[index] == color:
                resistor_value += str(number)
                break
    return int(resistor_value)