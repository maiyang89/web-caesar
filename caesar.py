def alphabet_position(letter):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alphabet_lower:
        return alphabet_lower.index(letter)
    if letter in alphabet_upper:
        return alphabet_upper.index(letter)
    return letter

def rotate_character(char,rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet_position(char)

    if rot % 26 != 0 and rot <= 26 and char.isupper():
        if position + rot > 25:
            return alphabet_upper[position - 26 + rot]
        else:
            return alphabet_upper[position + rot]
    if rot % 26 != 0 and rot > 26 and char.isupper():
        if rot - 26 + position > 25:
            return alphabet_upper[rot - 26 + position - 26]
        else:
            return alphabet_upper[rot - 26 + position]
    if rot % 26 != 0 and rot <= 26 and char.islower():
        if position + rot > 25:
            return alphabet_lower[position - 26 + rot]
        else:
            return alphabet_lower[position + rot]
    if rot % 26 != 0 and rot > 26 and char.islower():
        if rot - 26 + position > 25:
            return alphabet_lower[rot - 26 + position - 26]
        else:
            return alphabet_lower[rot - 26 + position]
    if char.islower():
        return alphabet_lower[position]
    if char.isupper():
        return alphabet_upper[position]
    return position

def encrypt(text,rot):
    newMsg = ""
    for eachChar in text:
        newMsg = newMsg + rotate_character(eachChar,rot)
    return newMsg
