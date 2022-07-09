# Uses python3
def edit_distance(s, t):
    # 0. add a " " to s and t to make it easier for me
    # 1. Initalize s+1 x t+1 matrix of zeros
    # 2. Fill first row and column with 0:s, 0:t
    # 3. iterate row through row to fill
    s = " " + s
    t = " " + t
    # print("s: {}, len(s): {}".format(s, len(s)))
    # print("t: {}, len(t): {}".format(t, len(t)))
    A = [[0 for i in range(len(t))] for j in range(len(s))]

    for i in range(len(t)): # set first row
        A[0][i] = i

    for j in range(len(s)): # set first column
        A[j][0] = j

    for j in range(len(s)):
        for i in range (len(t)):
            if i and j > 0:
                # left_case
                left_case = A[j][i-1]+1
                # above case
                right_case = A[j - 1][i]+1
                # diagonal case
                if s[j] == t[i]:
                    diagonal_case = A[j-1][i-1]
                else:
                    diagonal_case = A[j-1][i-1] + 1
                options = [left_case,right_case, diagonal_case]
                fill = min(options)
                A[j][i] = fill
    return A[-1][-1]


def test_algo():
    tc1 = edit_distance('short', 'ports')
    print(tc1)

    tc2 = edit_distance('abc', 'abc')
    print(tc2)

if __name__ == "__main__":
    test_algo()

    # print(edit_distance(input(), input()))
