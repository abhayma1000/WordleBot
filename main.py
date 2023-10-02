NUM_CHARS = 5


# Updates the list of banned characters
def update_banned_characters(banned_chars: list, placements: str) -> list:
    try:
        print("Enter characters combined as a string")
        element = input()
        for i in element:
            if i.isalpha() and i not in banned_chars and i not in placements:
                banned_chars.append(i.lower())
        print("Enter 0 to ignore, 1 to continue")
        stop = int(input())
        if stop == 0:
            raise RuntimeError
        else:
            return banned_chars

    except ValueError:
        print('You entered an invalid input')
    except RuntimeError:
        print("Cancelling process")

# Updates the placements of characters
def update_placements(banned_chars: list) -> str:
    try:
        print("Enter characters known and _ representing unknown characters")
        element = input().lower()
        new_element = ""
        for i in element:
            if i in banned_chars:
                raise ValueError
            if (i.isalpha() or i == "_"):
                new_element = new_element + "" + i.lower()
        if len(new_element) != NUM_CHARS:
            raise ValueError
        print("Enter 0 to ignore, 1 to continue")
        stop = int(input())
        if stop == 0:
            raise RuntimeError
        else:
            return new_element

    except ValueError:
        print('You entered an invalid input')
    except RuntimeError:
        print("Cancelling process")

# Updates the somewhere dictionary
def update_somewhere(somewhere: dict) -> dict:
    try:
        print("Enter character next to indices it is not in (0 indexing)")
        element = input().lower()
        if element[0].isalpha() and element[1:].isnumeric():
            if element[0].lower() not in somewhere.keys():
                somewhere[element[0].lower()] = []
            for num in element[1:]:
                if int(num) not in somewhere[element[0].lower()] and int(num) < NUM_CHARS:
                    somewhere[element[0].lower()].append(int(num))
        else:
            raise ValueError
        print("Enter 0 to ignore, 1 to continue")
        stop = int(input())
        if stop == 0:
            raise RuntimeError
        else:
            return somewhere

    except ValueError:
        print('You entered an invalid input')
    except RuntimeError:
        print("Cancelling process")

# Prints everything: banned characters, placements, somewhere dict
def print_data(banned_chars: list, placements: str, somewhere: dict):
    print(
        "Banned characters: " + str(banned_chars) + "\n" +
        "Placements: " + placements + "\n" +
        "Somewhere: " + str(somewhere)
    )

# Logic to compute possible words and output possible words
def get_word(banned_chars: list, placements: str, somewhere: dict, all_words: list):
    possible_words = []
    for word in all_words:
        # If none of the chars in all_words is in banned_chars
        if not any(char in word for char in banned_chars):

            # If the placements of "_" match the placements of the word
            skip = False
            for i in range(len(word)):
                if placements[i] != "_" and placements[i] != word[i]:
                    skip = True
            if not skip:
                keep = True
                somewhere_letters = list(somewhere.keys())
                for letter in somewhere_letters:
                    for letter_index in somewhere[letter]:
                        #if word doesnt have that character and that character is not in the indices
                        if letter not in word or word[letter_index] == letter:
                            keep = False
                if keep:
                    possible_words.append(word)
    
    print("Possible words: " + str(possible_words))

def main():
    # A list of banned characters. Each is a string in the list
    banned_characters = []

    # If the placement of a character is known, put in that index. Otherwise, put "_" in that index
    placements = "_____"

    # If a character is somewhere in word
    # The key is the character, value is list of indices it is not in
    somewhere = {}

    # A list of all five letter words in dictionary
    # Using dictionary from /usr/share/dict/web2
    word_path = "/usr/share/dict/web2"
    all_five_letter_words = []

    all_words = open(word_path).read().splitlines()

    for i in all_words:
        if len(i) == 5:
            all_five_letter_words.append(i.lower())
    
    all_five_letter_words = list(set(all_five_letter_words))

    # Handler code to see which action to take
    while True:
        try:
            print("""
            Enter 1 to update banned characters,
            2 to update placements,
            3 to update somewhere,
            4 to print data,
            5 to get possible words,
            0 to terminate program""")
            action = int(input())
            if action == 1:
                banned_characters = update_banned_characters(banned_characters, placements)
            elif action == 2:
                placements = update_placements(banned_characters)
            elif action == 3:
                somwehere = update_somewhere(somewhere)
            elif action == 4:
                print_data(banned_characters, placements, somewhere)
            elif action == 5:
                get_word(banned_characters, placements, somewhere, all_five_letter_words)
            elif action == 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid action. Restarting operation")

if __name__ == "__main__":
    main()