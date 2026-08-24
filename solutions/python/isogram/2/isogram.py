def is_isogram(phrase: str):
    phrase = [letter.lower() for letter in phrase if letter.isalpha()]
    return len(set(phrase)) == len(phrase)