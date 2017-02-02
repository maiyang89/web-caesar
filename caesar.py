import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase

    if letter in alphabet:
        return alphabet.index(letter)
    return letter

def rotate_character(char,rot):
    alphabet = string.ascii_uppercase
    position = alphabet_position(char.lower())

    #confirm if character is alphabetic
    if char.isalpha():
        #confirm if character is uppercase
        if char.isupper():
            #return the rotated character capitalized
            return alphabet[(position + rot) % len(alphabet)]
        else:
            #return the rotated character lowercased
            return string.ascii_lowercase[(position + rot) % len(alphabet)]
    #return character if not alphabetic
    else:
        return char

def encrypt(text,rot):
    newMsg = ""
    for eachChar in text:
        newMsg = newMsg + rotate_character(eachChar,rot)
    return newMsg
