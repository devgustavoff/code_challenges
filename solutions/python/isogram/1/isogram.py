def is_isogram(phrase: str):
    phrase = "".join([letter.lower() for letter in phrase if letter.isalpha()])
    for letter in phrase:
        if phrase.count(letter) > 1:
            return False

    return True