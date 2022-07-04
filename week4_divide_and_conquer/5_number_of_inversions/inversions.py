import sys


def merge(b, c):
    print("b: {}, c: {}".format(b,c))
    d = []
    while b and c:
        print(b, c)
        b1 = b[0]
        c1 = c[0]
        if b1 <= c1:
            d.append(b1)
            b.pop(0)
        else:
            d.append(c1)
            c.pop(0)
    if b:
        d += b
    elif c:
        d += c
    print("d: {}".format(d))
    return d


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return a
    ave = (left + right) // 2
    b = get_number_of_inversions(a, b, left, ave)
    c = get_number_of_inversions(a, b, ave, right)
    d = merge(b, c)
    return d


def merge_sort(a):
    print("a: {}".format(a))
    if len(a) <= 1:
        return a
    m = len(a)//2
    b = merge_sort(a[0:m])
    c = merge_sort(a[m:])
    a_prime = merge(b, c)
    return a_prime


def test_algo():

    # assert merge_sort([1, 3, 2, 4], [0, 0, 0, 0], 0, 4) == [1, 2, 3, 4],\
    #     merge_sort([1, 3, 2, 4], [0], 0, 4)
    assert merge_sort([1,3,2,4]) == [1,2,3,4], merge_sort([1,3,2,4])


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # print(n)
    # b = n * [0]
    # print(b)
    # print(get_number_of_inversions(a, b, 0, len(a)))
    test_algo()
