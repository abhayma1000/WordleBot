NUM_CHARS = 5

# Input code on how much stuff
"""
try:
    n = int(input())
    myList = []
    for i in range(n):
        element = input()
        myList.append(element)
    print('List :', myList)
except ValueError:
    print('You entered an invalid input')
"""


def update_banned_characters(banned_chars: list) -> list:
    try:
        print("Enter characters combined as a string")
        element = input()
        for i in element:
            if i.isalpha() and i not in banned_chars:
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

def print_everything(banned_chars: list, placements: str, somewhere: dict):
    print(
        "Banned characters: " + str(banned_chars) + "\n" +
        "Placements: " + placements + "\n" +
        "Somewhere: " + str(somewhere)
    )

def get_word():
    None

def main():
    # A list of banned characters. Each is a string in the list
    banned_characters = []

    # If the placement of a character is known, put in that index. Otherwise, put "_" in that index
    placements = "_____"

    # If a character is somewhere in word
    # The key is the character, value is list of indices it is not in
    somewhere = {}

    # Handler code to see which action to take
    while True:
        try:
            print("""Enter 1 to update banned characters,
            2 to update placements,
            3 to update somewhere,
            4 to print everything""")
            action = int(input())
            if action == 1:
                banned_characters = update_banned_characters(banned_characters)
            elif action == 2:
                placements = update_placements(banned_characters)
            elif action == 3:
                somwehere = update_somewhere(somewhere)
            elif action == 4:
                print_everything(banned_characters, placements, somewhere)
            else:
                raise ValueError
        except ValueError:
            print("Invalid action. Restarting operation")

if __name__ == "__main__":
    main()