import random

def vertical(letters, size, wordsearch):
    can_place_word = False
    while not can_place_word:
        row_num = random.randint(0, size - len(letters))
        column_num = random.randint(0, size - 1)

        can_place_word = True
        for i in range(len(letters)):
            if row_num + i >= size or wordsearch[row_num + i][column_num] != 0:
                can_place_word = False
                break
    if can_place_word:
        for i in range(len(letters)):
            wordsearch[row_num + i][column_num] = letters[i]


def horizontal(letters, size, wordsearch):
    can_place_word = False
    while not can_place_word:
        row_num = random.randint(0, size - 1)
        column_num = random.randint(0, size - len(letters))

        can_place_word = True
        for i in range(len(letters)):
            if column_num + i >= size or wordsearch[row_num][column_num + i] != 0:
                can_place_word = False
                break

    if can_place_word:
        for i in range(len(letters)):
            wordsearch[row_num][column_num + i] = letters[i]


def diagonal(letters, size, wordsearch):
    can_place_word = False
    while not can_place_word:
        row_num = random.randint(0, size - len(letters))
        column_num = random.randint(0, size - len(letters))

        can_place_word = True
        for i in range(len(letters)):
            if wordsearch[row_num + i][column_num + i] != 0:
                can_place_word = False
                break

    if can_place_word:
        for i in range(len(letters)):
            wordsearch[row_num + i][column_num + i] = letters[i]


def words_to_functions(fullwords, size, wordsearch):
    print(len(fullwords))
    r_full = random.randint(1, 2) # Orientation of vertical or horizontal only if words list == size of array

    for word in fullwords:
        letters = list(word) # Take list of fullwords and turn each word into a list of letters
        if len(fullwords) >= size - size*.33: # If the number of words exceeds 2/3 the size of the array, do not print diagonal words
            r = r_full
        else:
            r = random.randint(1, 3)  # Random number to randomize function

        if r == 1:
            vertical(letters, size, wordsearch)
        elif r == 2:
            horizontal(letters, size, wordsearch)
        elif r == 3:
            diagonal(letters, size, wordsearch)

        if not placed:
            for row in range(size):
                for col in range(size):
                    if wordsearch[row][col] == 0:
                        wordsearch[row][col] = letters[0]
                        break

        if wordsearch[row][col] != letters[0]:
            continue

        valid_placement = True
        for i in range(1, len(letters)):
            valid_placement = False
            break

        if valid_placement:
            for i in range(1, len(letters)):
                wordsearch[row][col + i] = letters[i]
        else:
            for i in range(1, len(letters)):
                if row + i >= size or (wordsearch[row + i][col != 0]) and wordsearch([row + i][col] != letters[i]):
                    return
                    wordsearch[row + i][col] = letters[i]


if __name__ == '__main__':
    size = int(input('Please enter the size for the wordsearch: '))  # size of square array
    wordsearch = [[0] * size for i in range(size)]  # initialize wordsearch array
    fullwords = []  # list for full words

    ''' This loop simply takes the words from the user and appends each word to fullwords list, stopping at 'done' '''
    while True:
        word = input("Enter a word, 'done' when finished:")
        word = word.upper()  # Convert word to uppercase
        if (word == 'done') | (word == 'DONE'):  # Break loop if user is done
            break
        if len(word) <= size:  # Ensures word is small enough to fit
            fullwords.append(word)
        else:
            print("The word you've typed is too large, please choose another word")

    '''Once all words are taken, try placing them'''
    words_to_functions(fullwords, size, wordsearch)

    '''Fill the rest of the grid with random characters'''
    for row in wordsearch:
        for i in range(len(row)):
            if row[i] == 0:
                randchar = chr(random.randint(65, 90))
                row[i] = randchar

    print("Word Search:")
    for row in wordsearch:
        print(*row)

    print("\nWords to Find:")
    for word in fullwords:
        print(word)