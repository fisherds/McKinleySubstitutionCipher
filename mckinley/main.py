def main():
    print("Hello McKinley!")
    # print("SUMMER", "0.1.2.2.3.4", get_pattern("SUMMER"))
    # print("MCKINLEY", "0.1.2.3.4.5.6.7", get_pattern("MCKINLEY"))
    # print("DAVID", "0.1.2.3.0", get_pattern("DAVID"))
    # f = open("mckinley/small_dict.txt", "r")
    # print(f.readline())
    # f.close()
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
    # print(word_pattern_dict)
    result = get_options("SUMMER", word_pattern_dict)
    print(result)

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








if __name__ == '__main__':
    main()
