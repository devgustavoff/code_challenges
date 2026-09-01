def value(colors):
    values = ['black', 'brown', 'red', 'orange', 'yellow', 
              'green', 'blue', 'violet', 'grey', 'white']
    tens = values.index(colors[0]) * 10
    units = values.index(colors[1])
    return tens + units