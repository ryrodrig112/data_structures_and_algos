# Uses python3
import sys
import random


def partition3(a, l=None, r=None):
    x = a[l]
    j = l
    j_len = 1
    for i in range(l+1, r+1):
        tmp = a[i]
        if a[i] < x:
            a.delete(i)
            a.insert(0, tmp)
            j += 1
        elif a[i] == x:
            j_len += 1
        else:
            pass
    return j, j_len


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


def test_partition():
    j, j_len = partition3([2, 2, 2, 3, 5, 1, 3, 0])
    assert j == 2, j
    assert j_len == 3, j_len


def test_qs():
    qs_test = randomized_quick_sort([2, 3, 9, 2, 2], 0, 4)
    assert  qs_test== [2,2,2,3, 9], qs_test


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    test_algo()
