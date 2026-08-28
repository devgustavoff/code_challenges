plain = "abcdefghijklmnopqrstuvwxyz"
cipher ="zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text: str):
    plain_text = "".join([char.lower() for char in plain_text if char.isalpha() or char.isalnum()])
    encode_list = []
    for char in plain_text:
        if char.isalpha():
            index = plain.find(char)
            encode_list.append(cipher[index])
        else:
            encode_list.append(char)

    encode_list = "".join(encode_list)

    if len(encode_list) > 5:
        counter = 0
        string_tmp = ""
        for char in encode_list:
            if counter == 5:
                string_tmp += " "
                counter = 0
            string_tmp += char
            counter += 1

        encode_list = string_tmp

    return encode_list

def decode(ciphered_text: str):
    ciphered_text = ciphered_text.split(" ")
    decode_list = []
    for string in ciphered_text:
        for char in string:
            if char.isalpha():
                char_index = cipher.find(char)
                decode_list.append(plain[char_index])
            else:
                decode_list.append(char)
    return "".join(decode_list)

print(encode("Testing,1 2 3, testing."))