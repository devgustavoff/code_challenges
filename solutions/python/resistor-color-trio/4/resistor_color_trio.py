def label(colors: list):
    values = ["black", "brown", "red", "orange", "yellow", 
              "green", "blue", "violet", "grey", "white"]

    tens = values.index(colors[0]) * 10
    units = values.index(colors[1])

    resistor_value = (tens + units) * (10**values.index(colors[2]))
    
    if resistor_value >= 1000 and resistor_value < 1000_000: # kiloohms
        return str(resistor_value // 1000) + " kiloohms"
    elif resistor_value >= 1000_000 and resistor_value < 1000_000_000: # megaohms
        return str(resistor_value // 1000_000) + " megaohms"
    elif resistor_value >= 1000_000_000: # gigaohms
        return str(resistor_value // 1000_000_000) + " gigaohms"
    
    return str(resistor_value) + " ohms"