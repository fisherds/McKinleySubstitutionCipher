# https://www.youtube.com/playlist?list=PLiEts138s9P1M9AUU7SCwt8ZkQRDGzSJQ
# 17. Basic Substitution cipher (no solving)
# https://www.youtube.com/watch?v=yJn_IaMXp04&list=PLiEts138s9P1M9AUU7SCwt8ZkQRDGzSJQ&index=17
# 18. Cracking (solving) a substitution cipher
# https://www.youtube.com/watch?v=sHoZiDeY-xM
# https://inventwithpython.com/cracking/chapter17.html

# Simple Substitution Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
import os, re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    # message = "Otter Creek Middle School"
    message = "Bccad Edaah Ijffga Kchool"  # Unsolvable by this algorithm.

    # message = """Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr
    #     sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa
    #     sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac
    #     ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx
    #     lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia
    #     rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh.
    #     -Facjclxo Ctrramm"""
    #
    # BTW the solution to the above is:
    # myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    
    # ciphered message from https://sefi.org/hsef/Display%20and%20Safety.pdf
    message = "Osrbmlh & Rlyajh Wpnnsjjaa Nsrrspx --> Jia nsrrspx py jisr wpnnsjjaa sr jp axrtca jilj lmm wpnbajsjpcr dtlmsyh ypc wpnbajsjspx lwwpcosxu jp jia ctmar arjlfmsriao sx wpxvtxwjspx esji jia Rwsaxjsysw Caqsae Wpnnsjjaa lxo Rpwsajh ypc Rwsaxwa. Jia IRAY Osrbmlh & Rlyajh sxrbawjspx bcpwarr wlx fa sxsjsljao pxmh eiax lmm sjanr lca bcaraxj lj jia osrbmlh. Jia Osrbmlh & Rlyajh Wpnnsjjaa esmm pyyac utsolxwa px Osrbmlh & Rlyajh srrtar ypc bcpvawjr lbbcpqao fh jia RCW jp wpnbaja sx IRAY. Pwwlrspxlmmh, jia IRAY Osrbmlh & Rlyajh Wpnnsjjaa nlh cadtsca rjtoaxjr jp nlka caqsrspxr jp wpxypcn jp Osrbmlh & Rlyajh cautmljspxr. Bacrsrjaxj srrtar esmm fa oscawjao jp l wpnnsjjaa py sxosqsotlmr eiswi nlh sxwmtoa RAYS bacrpxxam, Osrbmlh & Rlyajh (O&R) lxo/pc Rwsaxjsysw Caqsae Wpnnsjjaa (RCW) agawtjsqa wpnnsjjaa nanfacr. Jia ypmmpesxu cautmljspxr ntrj fa loiacao jp eiax l rjtoaxj agisfsjr l bcpvawj lj IRAY. Lmm bcpvawjr ntrj loiaca jp jia Osrbmlh & Rlyajh cadtscanaxjr py jia lyysmsljao ylsc(r) sx eiswi jiah wpnbaja. Kxpemaoua py jiara cadtscanaxjr sr jia carbpxrsfsmsjh py jia Ysxlmsrj, Lotmj Rbpxrpc, lxo Ylsc Oscawjpc."
    # BTW the solution to the above is:
    # message = "Display and Safety Committee Mission --> " \
	# 			+ "The mission of this committee is to ensure that all competitors qualify for competition according to the " \
	# 			+ "rules established in conjunction with the Scientific Review Committee and Society for Science. " \
	# 			+ "The HSEF Display & Safety inspection process can be initiated only when all items are present at the " \
	# 			+ "display. The Display & Safety Committee will offer guidance on Display & Safety issues for projects " \
	# 			+ "approved by the SRC to compete in HSEF. Occasionally, the HSEF Display & Safety Committee may " \
	# 			+ "require students to make revisions to conform to Display & Safety regulations. Persistent issues will be " \
	# 			+ "directed to a committee of individuals which may include SEFI personnel, Display & Safety (D&S) " \
	# 			+ "and/or Scientific Review Committee (SRC) executive committee members. " \
	# 			+ "The following regulations must be adhered to when a student exhibits a project at HSEF. All projects " \
	# 			+ "must adhere to the Display & Safety requirements of the affiliated fair(s) in which they compete. " \
	# 			+ "Knowledge of these requirements is the responsibility of the Finalist, Adult Sponsor, and Fair Director."

    print('Getting the letter mapping based on word patterns.')
    letterMapping = hackSimpleSub(message)

    # Display the results to the user:
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    # print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    # pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping:
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
        'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
        'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
        'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # The letterMapping parameter takes a dictionary value that
    # stores a cipherletter mapping, which is copied by the function.
    # The cipherword parameter is a string value of the ciphertext word.
    # The candidate parameter is a possible English word that the
    # cipherword could decrypt to.

    # This function adds the letters in the candidate as potential
    # decryption letters for the cipherletters in the cipherletter
    # mapping.

    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])

def intersectMappings(mapA, mapB):
    # To intersect two maps, create a blank map and then add only the
    # potential decryption letters if they exist in BOTH maps:
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:
        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely:
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter],
            # add that letter to intersectedMapping[letter]:
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping

def removeSolvedLettersFromMapping(letterMapping):
    # Cipherletters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other letter.
    # (This is why there is a loop that keeps reducing the map.)
    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # solvedLetters will be a list of uppercase letters that have one
        # and only one possible mapping in letterMapping:
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, then it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again:
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word:
        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping:
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping:
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Remove any solved letters from the other lists:
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an underscore.

    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key:
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()