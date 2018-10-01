# -*- coding: utf-8 -*-
#
# http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
# happy numbers up to 1000.
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)


def find_overlapping(file1, file2):
    common = []
    list1 = read_file_to_list(file1)
    list2 = read_file_to_list(file2)
    for number in list1:
        if number in list2 and number not in common:
            common.append(number)
    print "Numbers in file 1: ", (list1)
    print "Numbers in file 2: ", (list2)
    print "Overlapping numbers in both file 1 and 2: ", (common)


def read_file_to_list(file_name):
    number_list = []
    with open(file_name, 'r') as open_file:
        line = open_file.readline()
        while line:
            number_list.append(int(line))
            line = open_file.readline()
    return number_list


# main to run the task
if __name__ == "__main__":
    find_overlapping("primenumbers.txt", "happynumbers.txt")
