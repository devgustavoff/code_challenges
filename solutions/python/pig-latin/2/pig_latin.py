def rule_one(word: str) -> str:
    word += "ay"
    return word

def rule_two(index_vowel: int, consonants: list, word: str) -> str:
    consonants = "".join(consonants)
    word = word[index_vowel:] + consonants + "ay"
    return word

def rule_three(letter_index: int, consonants: list, word:str) -> str:
    consonants = "".join(consonants)
    word = word[letter_index:] + consonants + "qu" + "ay"
    return word

def rule_four(index_letter: int, consonants: list, word: str) -> str:
    if not consonants:
        word = word[index_letter+1:] + "y" + "ay"
        return word
    consonants = "".join(consonants)
    word = word[index_letter:] + consonants + "ay"
    return word

def translate(text):
    words = text.rsplit(" ")

    vowels = ["a", "e", "i", "o", "u"]
    prefixes = ["xr", "yt"]

    consonants = []
    result = list()

    for word in words:
        if word[0] in vowels or word[:2] in prefixes:
            word = rule_one(word=word)
            result.append(word)
            continue

        for letter in word:
            if letter in vowels: # Rule 2
                word = rule_two(index_vowel=word.find(letter), consonants=consonants, word=word)
                result.append(word)
                consonants.clear()
                break
            elif letter == "y": # Rule 4
                word = rule_four(index_letter=word.find(letter), consonants=consonants, word=word)
                result.append(word)
                consonants.clear()
                break
            elif letter == "q" and word[word.find(letter) + 1] == "u": # Rule 3
                word = rule_three(letter_index=word.find(letter) + 2, consonants=consonants, word=word)
                result.append(word)
                consonants.clear()
                break
            consonants.append(letter)

    return " ".join(result)

# VOWELS = {"a", "e", "i", "o", "u"}
# VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
# SPECIALS = {"xr", "yt"}


# def translate(text):
#     piggyfied = []

#     for word in text.split():
#         if word[0] in VOWELS or word[0:2] in SPECIALS:
#             piggyfied.append(word + "ay")
#             continue

#         for pos in range(1, len(word)):
#             if word[pos] in VOWELS_Y:
#                 pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
#                 piggyfied.append(word[pos:] + word[:pos] + "ay")
#                 break

#     return " ".join(piggyfied)

# print(translate("yellow"))