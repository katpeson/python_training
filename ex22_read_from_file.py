# -*- coding: utf-8 -*-
#
#  http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,..
#  and print out the results to the screen.
#
# Extra:
# Instead of using the .txt file from above (or instead of, if you want the challenge),
# take this .txt file, and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene recognition database,
#  and lists the file directory hierarchy for the images. Once you take a look at the first line or
#  two of the file, it will be clear which part represents the scene category. To do this, you’re going
#  to have to remember a bit about string parsing in Python 3.


# reads the given file (in param) and returns all content as string
def read_from_file(file_name):
    with open(file_name, 'r') as open_file:
        all_text = open_file.read()
    return all_text


# counts all names in given string and returns a dictionary with name as key and count...
# ... of the name in the string
def count_names_in_string(text_param):
    name_list = text_param.splitlines()
    name_dict = {}
    for name in name_list:
        if name not in name_dict:
            name_dict[name] = 1
        else:
            name_dict[name] += 1
    return name_dict


# prints given dictionary as {key, value}
def print_dictionary(dictionary):
    # for n, i in dictionary.items():
    #     print(n, i)
    #
    for pair in dictionary.items():
        print(pair)


# EXTRA
def get_categories(file_name):
    cat_dict = {}
    with open(file_name, 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line[3:-26]
            if line not in cat_dict:
                cat_dict[line] = 1
            else:
                cat_dict[line] += 1
            line = open_file.readline()
    return cat_dict


# main to run the task
if __name__ == "__main__":
    # BASIC TASK
    # using nameslist.txt as that was in the example and it's located in same file as this python file
    print "Printing the count of names from given file"
    text = read_from_file('nameslist.txt')
    names_count_dict = count_names_in_string(text)
    print_dictionary(names_count_dict)
    # EXTRA TASK
    print "Printing the count of categories from given sun file"
    print_dictionary(get_categories('Training_01.txt'))

