def counting_words() -> dict:
    try:
        with open("Texto.txt", "r") as f:
            lines = f.readlines()
            words_dict = {}    # dictionary to keep track of how many times each word appears
            for line in lines:
                words = line.split()
                for word in words:
                    word = verify_special_char(word)
                    if word in words_dict.keys():
                        words_dict[word] += 1
                    else:
                        words_dict[word] = 1
    except OSError:
        print(f"Could not open the file")
        exit()

    f.close()
    return words_dict

def verify_special_char(word) -> str:
    word = word.lower()   # considering all cases as lower, once we should not differentiate upper and lower cases
    last_char_ord = ord(word[-1])
    if last_char_ord < 97 or last_char_ord > 122: # if the last character is a special character (not between 'a' and 'z')
        word = word[:len(word) - 1]    # removing the last character
    return word

# printing function to 
def words_print(dictionary: dict) -> None:
    counter = 0
    for key, value in dictionary.items():
        if counter < 4:
            print(f'{key}: {value}    ', end="")
            counter += 1
        else:
            print("\n", end="")
            print("-------------------" * 4)
            print(f'{key}: {value}    ', end="")
            counter = 0
    
def main():
    words_dictionary = counting_words()
    words_print(words_dictionary)
    
main()
