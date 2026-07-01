import collections 

def transform(legacy_data):
    data = {}
    for key in legacy_data:
        for value in legacy_data[key]:
            data[value.lower()] = key 
    return data

print(transform({1: ["A", "E"], 2: ["D", "G"]}))