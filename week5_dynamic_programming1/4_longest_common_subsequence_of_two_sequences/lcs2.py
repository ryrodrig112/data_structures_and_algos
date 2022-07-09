#Uses python3

import sys

def lcs2(a, b):
    #0. fix 0's to the start of each string
    #1. Create A starting with all zeros
    #2. iterate through A by taking the max of the values to the left unless a[i] == b[j] then +1

    a.insert(0,None)
    b.insert(0, None)
    A = [[0 for i in range(len(b))] for j in range(len(a))]

    for j in range(len(a)):
        for i in range(len(b)):
            if i > 0:
                left_case = A[j][i-1]
                above_case = A[j-1][i]
                diagonal_case = A[j-1][i-1]

                if a[j] == b[i]:
                    fill = max([left_case, above_case, diagonal_case]) + 1
                else:
                    fill = max([left_case, above_case, diagonal_case])
                A[j][i] = fill
    print(a,b, A[-1][-1])
    return A[-1][-1]

def test_algo():
    tc1 = lcs2([1,2,3], [1,2,3,4,])
    assert tc1 == 3, tc1

    tc2 = lcs2([7], [1,2,3,4])
    assert tc2 ==0, tc2

    tc3 = lcs2([2,7,8,3], [5,2,8,7])
    assert tc3 == 2, tc3

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    #
    # n = data[0]
    # data = data[1:]
    # a = data[:n]
    #
    # data = data[n:]
    # m = data[0]
    # data = data[1:]
    # b = data[:m]
    #
    # print(lcs2(a, b))
    test_algo()
