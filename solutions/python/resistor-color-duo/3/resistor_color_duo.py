def value(colors):
    values = ['black', 'brown', 'red', 'orange', 'yellow', 
              'green', 'blue', 'violet', 'grey', 'white']
    return int(str(values.index(colors[0])) + str(values.index(colors[1])))