#Uses python3

import sys

def lcs3(a, b, c):
    # fix blanks to the front of a, b, c
    # create 3d matrix a that is a tall, b wide, c deep
    # iterate through but each spot has to equal eachother
    for list in [a, b, c]:
        list.insert(0, None)
    # print("a: {}, b: {}, c: {}". format(a, b, c))
    height = len(a)
    width = len(b)
    depth = len(c)
    A = [[[0 for x in range(width)] for y in range(height)] for z in range(depth)]  # create A
    for z in range(depth): # iterate through A, starting at the front, and moving left, then down, then back
        for y in range(height):
            for x in range(width):
                if x and y and z > 0:
                    # 2d first, need left and right
                    left_case = A[z][y][x-1]
                    above_case = A[z][y-1][x]
                    depth_case = A[z-1][y][x]
                    options = [left_case, above_case, depth_case]
                    if a[y] == b[x] == c[z]:
                        fill = max(options) + 1
                    else:
                        fill = max(options)
                    A[z][y][x] = fill
    return A[-1][-1][-1]


def test_algo():
    tc1 = lcs3([1], [1,2], [3,1,2])
    assert tc1 == 1, tc1

    tc2 = lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5])
    assert tc2 == 2, tc2

    tc3 = lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])
    assert tc3 == 3, tc3


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # an = data[0]
    # data = data[1:]
    # a = data[:an]
    # data = data[an:]
    # bn = data[0]
    # data = data[1:]
    # b = data[:bn]
    # data = data[bn:]
    # cn = data[0]
    # data = data[1:]
    # c = data[:cn]
    # print(lcs3(a, b, c))
    test_algo()
