def proverb(*input_data, qualifier):
    proverbial = []

    if not input_data:
        return proverbial
    
    for index, _ in enumerate(input_data):
        if index + 1 < len(input_data):
            a, b = input_data[index], input_data[index + 1]
            proverbial.append(f"For want of a {a} the {b} was lost.")

    if qualifier:
        proverbial.append(f"And all for the want of a {qualifier} {input_data[0]}.")
    else:
        proverbial.append(f"And all for the want of a {input_data[0]}.")

    return proverbial