# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# Important learning here: don't forget split unless you want to revert the whole string as a list of characters!


# takes list and returns it in reversed order
# used here the explanation of extended slices from: https://docs.python.org/2.3/whatsnew/section-slices.html
def return_reversed(a_list):
    return " ".join(a_list[::-1])


# asks user for input, returns the split input in list
def get_input(prompt="Provide me a long string: "):
    return raw_input(prompt).split()


print return_reversed(get_input())
