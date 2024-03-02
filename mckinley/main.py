# This function is called main, it calls all the other functions and as the 
# name implies it is the main function of the program
def main():
    # Creates dictionaries called master_key and word_pattern_dict
    master_key = {}
    word_pattern_dict = {}

    # This opens the text file of the dictionary of 45,000 words and gets the 
    # pattern for each word using the get_pattern function
    with open('mckinley/dictionary.txt') as f:
        for word in f:
            word = word.strip()
            pattern = get_pattern(word)

            # This adds to a new dictionary of every word and its pattern
            if pattern in word_pattern_dict:
                word_pattern_dict[pattern].append(word)
            else:
                word_pattern_dict[pattern] = [word]
    
    # This opens the text file with the encrypted sample in it 
    with open('mckinley/secret01.txt') as f:
        text = f.read()
        words = text.split(' ')
    
    # This gets the options for each letter from the get_options function
    for word in words:
        result = get_options(word, word_pattern_dict)
        
        # This means that if there is no options just continue with the code
        if result == -1:
            continue

        # This merges the options for each letter to the master key using the
        # merge_results function
        merge_results(master_key, result)

    for cipher_letter in master_key:
        try:
            plaintext_letter_options = list(master_key[cipher_letter])
        except KeyError:
            continue

        # This prints each letter and whether or not it was decrpyted
        if len(plaintext_letter_options) == 1:
            print("We know that the cipher letter " + cipher_letter + 
                  " is really a " + plaintext_letter_options[0])
        else:
            print("Not sure about " + cipher_letter + " it could be " 
                  + str(plaintext_letter_options))

    # This section prints the decrypted message
    translated = ""
    for cipher_letter in text:
        if cipher_letter == " ":
            translated += " "
            continue

        try:
            plaintext_letter_options = list(master_key[cipher_letter])
        except KeyError:
            continue
        
        # Checks if the cipher letters have been decrypted and if they have the letter
        # is added to the final message that will be displayed on the terminal
        if len(plaintext_letter_options) == 1:
            translated += plaintext_letter_options[0]
        # If there is more than one option or no options that letter is marked with a '.'
        else:
            translated += "."

    # This prints the decrpyted message
    print(translated) 
        
# This function is called get_pattern and it finds the pattern of each word in the 
# encrypted sample
def get_pattern(word):
    # This sets up some variables that will be used in this function
    amount = len(word)
    next_num = 0
    letter_dict = {}
    word_pattern = ""
    
    # This runs this loop based on how many letters are in the word
    for index_num in range(amount):
        current_letter = word[index_num]
        was_found = False
        
        for checker_index in range(index_num):
            if checker_index == index_num:
                continue
            if current_letter == word[checker_index]:
                was_found = True

        # This creates the pattern and in between each number in the pattern adds a '.'
        if was_found:
            # If the letter is a duplicate of a previous letter it uses the same number
            word_pattern += str(letter_dict[current_letter]) + '.' 
        else:
            # If the letter isn't a duplicate of a previous letter it uses the next number
            word_pattern += str(next_num) + '.' 
            letter_dict[current_letter] = next_num
            next_num += 1
    
    # This returns the pattern of word to the main function
    return word_pattern

# This function is called get_options and it gets the options for each letter based on
# the pattern of the word and what words in the 45,000 word dictornary match with it
def get_options(ciphertext, word_pattern_dict):
    pattern = get_pattern(ciphertext)
    
    # If the pattern isn't in the dictornary it just disregards that word
    if pattern not in word_pattern_dict:
        return -1
    
    options_list = word_pattern_dict[pattern]
    options_dict = {}
    
    for letter in ciphertext:
        options_dict[letter] = set()

    # This is finding what each letter could be based on what patterns matched with the
    # word pattern
    for option in options_list:
        for k in range(len(option)):
            letter_in_ciphertext = ciphertext[k]
            letter_in_option = option[k]
            set_for_letter = options_dict[letter_in_ciphertext]
            set_for_letter.add(letter_in_option)
    
    # This returns the options for each letter
    return options_dict

# This function is called merge_results and it merges the results for the get_options
# function to the master key
def merge_results(master_key, options_dict):
    for key in options_dict:
        if key in master_key:
            master_key[key] = master_key[key].intersection(options_dict[key])
        else:
            master_key[key] = options_dict[key]
            

# This calls main so the program runs
if __name__ == '__main__':
    main()
