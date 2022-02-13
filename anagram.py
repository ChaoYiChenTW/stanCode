"""
File: anagram.py
Name: Elaine Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm
import string

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
words = {}                    # Dictionary
pairs = {}                    # Two-letter combinations that never occur in dictionary


def main():
    """
    TODO:
    """
    read_dictionary()
    searchPairs()
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        find_anagrams(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    to make a dictionary classified by the length of words and the first letter
    """
    global words
    wordsList = []
    with open(FILE, 'r') as f:
        wordsList += f.read().split()
    for word in wordsList:
        if len(word) not in words:
            words[len(word)] = {}
            words[len(word)][word[0]] = [word]
        elif word[0] not in words[len(word)]:
            words[len(word)][word[0]] = [word]
        else:
            words[len(word)][word[0]].append(word)



def find_anagrams(s):
    """
    :param s: the word to search
    """
    print('Searching...')
    ansList = []
    ans = ''
    find_anagrams_helper(s, ansList, ans)
    print(f'{len(ansList)} anagrams: {ansList}')
    

def find_anagrams_helper(s, ansList, ans):
    """
    :param s      : the word to search
    :      ansList: a list including all anagrams
    :      ans    : a word to search if it is in dictionary
    """
    global words
    if len(ans) == len(s):
        if ans in words[len(s)][ans[0]] and ans not in ansList:
            print('Found: ', ans)
            ansList.append(ans)
            print('Searching...')
        return
    else:
        for ele in s:
            if ans.count(ele) < s.count(ele):
                ans += ele
                if has_prefix(ans):
                    ans = ans[:-1]
                    continue
                find_anagrams_helper(s, ansList, ans)
                ans = ans[:-1]        


def has_prefix(sub_s):
    """
    :param sub_s: a string to search
    :return: boolean, if sub_s is in pairs
    """
    global pairs
    if sub_s in pairs[sub_s[0]]:
        return True


def searchPairs():
    """
    to find all two-letter combinations that never occur in dictionary
    """
    global words
    global pairs
    for alp1 in string.ascii_lowercase:
        pairs[alp1] = []
        for alp2 in string.ascii_lowercase:
            pairs[alp1].append(alp1 + alp2)

    for key1 in words:
        if key1 == 1:
            continue
        for key2 in words[key1]:
            for word in words[key1][key2]:
                if word[:2] in pairs[key2]:
                    pairs[key2].remove(word[:2])



if __name__ == '__main__':
    main()
