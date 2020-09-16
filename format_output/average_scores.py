"""
Program: average_scores.py
Author: Jack Reser

program that accepts 3 test scores, first and last name, and age.  Prints out info
"""


def average():
    score1 = input("Enter your first score: ")
    score2 = input("Enter your second score: ")
    score3 = input("Enter your third score: ")

    return (int(score1) + int(score2) + int(score3)) / 3

if __name__ == '__main__':
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    age = input("Enter your age: ")
    average_scores = average()

    print("{}, {} age: {} average grade: {}".format(last_name, first_name, age, average_scores))


#Test scores: (80, 85, 90)  First: Jack  Last: Reser  Age: 22
# Output: Reser, Jack age: 22 average grade: 85.0
