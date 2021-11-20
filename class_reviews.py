"""
File: class_reviews.py
Name: Elaine Chen
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""
import sys

def main():
    """
    Input
        className: str
        score: int
    Output
        the characteristics values of class SC001 and SC101
    """
    count001 = 0
    count101 = 0
    sum001 = 0
    sum101 = 0
    max001 = -999
    max101 = -999
    min001 = 999
    min101 = 999

    while True:
        className = input('Which class? ')
        if className == '-1': break
        score = int(input('Score: '))
        if className[2:5] == '001':
            count001 += 1
            sum001 += score
            if score > max001: max001 = score
            if score < min001: min001 = score
        elif className[2:5] == '101':
            count101 += 1
            sum101 += score
            if score > max101: max101 = score
            if score < min101: min101 = score
    if (count001 == 0) and (count101 == 0):
        print('No class scores were entered')
        sys.exit(0)
    print('=============SC001=============')
    if count001 == 0: print('No score for SC001')
    else:
        print('Max (001): ', max001)
        print('Min (001): ', min001)
        print('Avg (001): ', sum001/count001)
    print('=============SC101=============')
    if count101 == 0: print('No score for SC101')
    else:
        print('Max (101): ', max101)
        print('Min (101): ', min101)
        print('Avg (101): ', sum101/count101)


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
