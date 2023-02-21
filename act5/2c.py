def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("" . join(key))


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("" . join(cipher_text))


# Driver code
if __name__ == "__main__":
    print('Insert your string')
    encryptedString = input()
    print('Insert your Key')
    keyText = input()
    key = generateKey(encryptedString, keyText)
    cipher_text = cipherText(encryptedString, key)
    print("Ciphertext :", cipher_text)


#
