def main():
    print("Hello McKinley!")
    # print("SUMMER", "0.1.2.2.3.4", get_pattern("SUMMER"))
    # print("MCKINLEY", "0.1.2.3.4.5.6.7", get_pattern("MCKINLEY"))
    # print("DAVID", "0.1.2.3.0", get_pattern("DAVID"))
    # f = open("mckinley/small_dict.txt", "r")
    # print(f.readline())
    # f.close()
    master_key = {}
    word_pattern_dict = {}
    with open('mckinley/dictionary.txt') as f:
        for word in f:
            word = word.strip()
            pattern = get_pattern(word)
            # print(word)
            # print(pattern)
            if pattern in word_pattern_dict:
                word_pattern_dict[pattern].append(word)
            else:
                word_pattern_dict[pattern] = [word]
    
    with open('mckinley/secret01.txt') as f:
        text = f.read()
        words = text.split(' ')
    
    for word in words:
        result = get_options(word, word_pattern_dict)
        if result == -1:
            continue
        merge_results(master_key, result)

    # print(word_pattern_dict)
    # result = get_options("ABCCDE", word_pattern_dict)
    # merge_results(master_key, result)
    # print("ABCCDE", master_key)
    # print()
    # # result = get_options("ABC", word_pattern_dict)
    # merge_results(master_key, {"A": {"Z", "Q"}})
    # print("fake", master_key)
    # # result = get_options("CDED", word_pattern_dict)
    # merge_results(master_key, result)
    # print(master_key)

    # Print results info:
    for cipher_letter in master_key:
        plaintext_letter_options = list(master_key[cipher_letter])
        if len(plaintext_letter_options) == 1:
            print("We know that the cipher letter " + cipher_letter + " is really a " + plaintext_letter_options[0])
        else:
            print("Not sure about " + cipher_letter + " it could be " + str(plaintext_letter_options))

    translated = ""
    for cipher_letter in text:
        if cipher_letter == " ":
            translated += " "
            continue
        plaintext_letter_options = list(master_key[cipher_letter])
        if len(plaintext_letter_options) == 1:
            translated += plaintext_letter_options[0]
        else:
            translated += "."

    print(translated) 
        

def get_pattern(word):
    amount = len(word)
    next_num = 0
    letter_dict = {}
    word_pattern = ""
    for index_num in range(amount):
        current_letter = word[index_num]
        was_found = False
        for checker_index in range(index_num):
            if checker_index == index_num:
                continue
            if current_letter == word[checker_index]:
                was_found = True
            
        if was_found:
            word_pattern += str(letter_dict[current_letter]) + '.' 
        else:
            word_pattern += str(next_num) + '.' 
            letter_dict[current_letter] = next_num
            next_num += 1
    return word_pattern
    
def get_options(ciphertext, word_pattern_dict):
    pattern = get_pattern(ciphertext)
    if pattern not in word_pattern_dict:
        return -1
    options_list = word_pattern_dict[pattern]
    options_dict = {}
    for letter in ciphertext:
        options_dict[letter] = set()
    for option in options_list:
        for k in range(len(option)):
            letter_in_ciphertext = ciphertext[k]
            letter_in_option = option[k]
            set_for_letter = options_dict[letter_in_ciphertext]
            set_for_letter.add(letter_in_option)
    
    return options_dict

def merge_results(master_key, options_dict):
    for key in options_dict:
        # print(key)
        # print(options_dict[key])
        if key in master_key:
            # print('letter found', key)
            master_key[key] = master_key[key].intersection(options_dict[key])
        else:
            # print('letter not found')
            master_key[key] = options_dict[key]
            








if __name__ == '__main__':
    main()
