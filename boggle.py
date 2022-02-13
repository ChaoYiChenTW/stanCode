"""
File: boggle.py
Name: Elaine Chen
----------------------------------------
TODO: to search words from input letters
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():

    start = time.time()
    # to store the dictionary into a Python list called words
    words = read_dictionary()
    
    # input letters
    row1 = tuple(input('1 row of letters: ').lower().split())
    # if input format is not acceptable, end the program
    if isIlligal(row1):
        print('Illegal input')
        exit(0)
    row2 = tuple(input('2 row of letters: ').lower().split())
    if isIlligal(row2):
        print('Illegal input')
        exit(0)
    row3 = tuple(input('3 row of letters: ').lower().split())
    if isIlligal(row3):
        print('Illegal input')
        exit(0)
    row4 = tuple(input('4 row of letters: ').lower().split())
    if isIlligal(row4):
        print('Illegal input')
        exit(0)
    # use tuple to increase efficiency
    rows = (row1, row2, row3, row4)
    
    # a list collects all answers
    wordList = []
    # pick an initial point
    for i in range(len(rows)):
        for j in range(len(rows)):
            word = ''
            passed = []      
            search(i, j, rows, passed, word, wordList, words)
    print(f'There are {len(wordList)} words in total.')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search(i, j, rows, passed, word, wordList, words):
    """
    <Input>
    i: int, an index of the initial point
    j: int, an index of the initial point
    rows: 4*4 nested tuple, input letters
    passed: list, a list records passed letters
    word: str, picked letters
    wordlist: list, all picked words that is in the dictionary
    words: list, dictionary
    <To-Do>
    to search word
    """
    word += rows[i][j]
    passed.append((i, j))
    possibleWords = [a for a in words if word == a[:len(word)]]
    if not possibleWords:
        return
    if len(word) >= 4:
        if word in possibleWords and word not in wordList:
            print(f'Found "{word}"')
            wordList.append(word)
    # up
    if j-1 >= 0 and (i, j-1) not in passed:
        search(i, j-1, rows, passed, word, wordList, words)
        passed.pop()
    # down
    if j+1 <= 3 and (i, j+1) not in passed:
        search(i, j+1, rows, passed, word, wordList, words)
        passed.pop()
    # left
    if i-1 >= 0 and (i-1, j) not in passed:
        search(i-1, j, rows, passed, word, wordList, words)
        passed.pop()
    # right
    if i+1 <= 3 and (i+1, j) not in passed:
        search(i+1, j, rows, passed, word, wordList, words)
        passed.pop()
    # upperleft
    if i-1 >= 0 and j-1 >= 0 and (i-1, j-1) not in passed:
        search(i-1, j-1, rows, passed, word, wordList, words)
        passed.pop()
    # lowerleft
    if i-1 >= 0 and j+1 <= 3 and (i-1, j+1) not in passed:
        search(i-1, j+1, rows, passed, word, wordList, words)
        passed.pop()
    # upperright
    if i+1 <= 3 and j-1 >= 0 and (i+1, j-1) not in passed:
        search(i+1, j-1, rows, passed, word, wordList, words)
        passed.pop()
    # lowerright
    if i+1 <= 3 and j+1 <= 3 and (i+1, j+1) not in passed:
        search(i+1, j+1, rows, passed, word, wordList, words)
        passed.pop()
    

def isIlligal(row):
    """
    <Input>
    row: str, input letters
    <To-Do>
    to determine whether the input is acceptable
    """
    if len(row) != 4:
        return True
    for ele in row:
        if len(ele) != 1 or not ele.isalpha():
            return True


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        words = f.read().split()
    return words


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    pass


if __name__ == '__main__':
    main()
