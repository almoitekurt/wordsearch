if __name__ == "__main__":
    import string
    import random

    size = 11
    wordsearch = [[0] * size for _ in range(size)]

    # ******************** Vertical Word ************************


    word1 = "UPDOWN"
    word1_letters = list(word1)

    can_place_word = False
    while not can_place_word:
        row_Num = random.randint(0, size - 1)
        column_Num = random.randint(0, size - len(word1_letters))

        can_place_word = True
        for i in range(len(word1_letters)):
            if row_Num + i >= size or wordsearch[row_Num + i][column_Num] != 0:
                can_place_word = False
                break

    if can_place_word:
        for i in range(len(word1_letters)):
            wordsearch[row_Num + i][column_Num] = word1_letters[i]

    print("**********************************")

    for row in wordsearch:
        print(row)

    # ******************** Horizontal Word  ************************

    word2 = "ACROSS"
    word2_letters = list(word2)

    can_place_word = False
    while not can_place_word:
        row_Num = random.randint(0, size - 1)
        column_Num = random.randint(0, size - len(word2_letters))

        can_place_word = True
        for i in range(len(word2_letters)):
            if column_Num + i >= size or wordsearch[row_Num][column_Num + i] != 0:
                can_place_word = False
                break

    if can_place_word:
        for i in range(len(word2_letters)):
            wordsearch[row_Num][column_Num + i] = word2_letters[i]

    print("**********************************")

    for row in wordsearch:
        print(row)

    # ******************** Diagonal Word ************************

    word3 = "DIAGONAL"
    word3_letters = list(word3)

    can_place_word = False
    while not can_place_word:
        row_Num = random.randint(0, size - len(word3_letters))
        column_Num = random.randint(0, size - len(word3_letters))

        can_place_word = True
        for i in range(len(word3_letters)):
            if wordsearch[row_Num + i][column_Num + i] != 0:
                can_place_word = False
                break

    if can_place_word:
        for i in range(len(word3_letters)):
            wordsearch[row_Num + i][column_Num + i] = word3_letters[i]

    print("**********************************")

    for row in wordsearch:
        print(row)

    # ******************** Fill rest of 0s with characters ************************

    print("**********************************")

    for row in wordsearch:
        print(row)

    for item in wordsearch:
        for i in range(len(item)):
            randchar = chr(random.randint(65, 90))
            if item[i] == 0:
                item[i] = randchar

    print("**********************************")

    for row in wordsearch:
        print(row)