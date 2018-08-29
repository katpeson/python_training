# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


def get_number(prompt="Tell me how many Fibonacci numbers you want: "):
    return int(input(prompt))


def generate_fibonacci(number):
    if number == 0:
        return []
    if number == 1:
        return [1]
    elif number >= 2:
        f_list = [1, 1]
        if number > 2:
            # Because we already added two above!
            i = 1
            while i < (number-1):
                f_list.append(f_list[i] + f_list[i-1])
                i += 1
        return f_list


list = (generate_fibonacci(get_number()))
if not list:
    print "You didn't want any Fibonacci numbers"
else:
    print (list)

