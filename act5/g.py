import string


def main():
    encryptedWord = input()
    my_alphas = string.ascii_lowercase  # string of lowercase alphabates
    print('This is an encrypted word:', encryptedWord)

    for i in range(0, 26):
        decryptedWord = ''
        for e in encryptedWord:
            if (e != ' ' and e != '.'):
                lowerVersion = e.lower()
                decryptedChar = my_alphas.index(lowerVersion) + abs(i)
                if lowerVersion in my_alphas:
                    if (decryptedChar > len(my_alphas)):
                        decryptedChar -= 26

                decryptedWord += my_alphas[decryptedChar-1]

        print("This is the decrypted version for shift : ", i, decryptedWord, "\n")


if __name__ == '__main__':
    main()
