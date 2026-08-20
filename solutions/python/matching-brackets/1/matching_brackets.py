
def is_paired(input_string):
    stack = list()
    pairs = {
        "[": "]",
        "{": "}",
        "(": ")"
    }
    for char in input_string:
        if char in pairs:
            stack.append(char)

        if char in pairs.values() and (not stack or pairs[stack[-1]] != char):
            return False

        if char in pairs.values() and pairs[stack[-1]] == char:
            stack.pop()

    return not stack