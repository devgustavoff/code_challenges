def proverb(*input_data, qualifier=None):
    proverbial = []

    for element_a, element_b in zip(input_data, input_data[1:]):
        proverbial.append(f"For want of a {element_a} the {element_b} was lost.")
    
    if qualifier:
        proverbial.append(f"And all for the want of a {qualifier} {input_data[0]}.")
    else:
        if input_data:
            proverbial.append(f"And all for the want of a {input_data[0]}.")

    return proverbial