def rot13(text):
    result = ''
    for char in text:
        if char.isalpha(): # ignore non-alphabet
            offset = 13 if char.islower() else -13
            new_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26) + ord('a' if char.islower() else 'A'))
        else:
            new_char = char
        result += new_char
    return result

if __name__ == "__main__":
    text = input("")
    print(rot13(text))
