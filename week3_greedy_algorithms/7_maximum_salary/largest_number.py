#Uses python3

import sys

def largest_number(a):
    #write your code here
    #  1. Loop through each item in a
    #  2. Find the number that leads to the highest number?
    #  3. Remove that number from a
    res = ""
    str_numbers = [str(number) for number in a]
    while str_numbers:
        selection = str_numbers[0]
        for num in str_numbers:
            if int(num + selection) >= int(selection + num):
                selection = num
        str_numbers.remove(selection)
        res += selection

    return int(res)


def test_algo():
    assert largest_number([21, 2]) == 221, largest_number([21, 2])
    assert largest_number([9, 4, 6, 1, 9]) == 99641, largest_number([9, 4, 6, 1, 9])
    assert largest_number([23, 39, 92]) == 923923, largest_number([23, 39, 92])
    assert largest_number([9, 11, 338]) == 933811, largest_number([9, 11, 338])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    # test_algo()
    
