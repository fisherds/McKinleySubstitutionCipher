# Simple Substitution Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    myMessage = "Display and Safety Committee Mission " \
				+ "The mission of this committee is to ensure that all competitors qualify for competition according to the " \
				+ "rules established in conjunction with the Scientific Review Committee and Society for Science. " \
				+ "The HSEF Display & Safety inspection process can be initiated only when all items are present at the " \
				+ "display. The Display & Safety Committee will offer guidance on Display & Safety issues for projects " \
				+ "approved by the SRC to compete in HSEF. Occasionally, the HSEF Display & Safety Committee may " \
				+ "require students to make revisions to conform to Display & Safety regulations. Persistent issues will be " \
				+ "directed to a committee of individuals which may include SEFI personnel, Display & Safety (D&S) " \
				+ "and/or Scientific Review Committee (SRC) executive committee members. " \
				+ "The following regulations must be adhered to when a student exhibits a project at HSEF. All projects " \
				+ "must adhere to the Display & Safety requirements of the affiliated fair(s) in which they compete. " \
				+ "Knowledge of these requirements is the responsibility of the Finalist, Adult Sponsor, and Fair Director."
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    # pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')


def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
