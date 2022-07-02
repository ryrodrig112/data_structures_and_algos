# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    j_len = 1
    for i in range(l+1, r+1):
        tmp = a[i]
        if a[i] < x:
            a.pop(i)
            a.insert(0, tmp)
            j += 1
        elif a[i] == x:
            j_len += 1
        else:
            pass
    j_end = j + j_len
    return j, j_end


def partition2(a, l, r):
    x = a[l]  # pivot value
    j = l  # initial pivot location
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1  # move pivot to the right
            a[i], a[j] = a[j], a[i]  # swap ith element with pivot
    a[l], a[j] = a[j], a[l] # put a [l] into the pivot location
    return j

def randomized_quick_sort2(a, l, r):
    print("a: {}, l: {}, r: {}".format(a, l, r))
    if l >= r :  # null
        return
    k = random.randint(l, r)  # pick a random index to be the pivot
    a[l], a[k] = a[k], a[l]  # switch a[l] and a[k] bc l is the pivot in partitions
    #use partition3
    print("k = {}, a = {}".format(k, a))
    j = partition2(a, l, r)  # find the partition point for the random index
    print("k = {}, m = {}, a: {}".format(k, j, a))
    print("Left Half: {}, l: {}, r: {}".format(a[l:j], l, j))
    print("Right Half: {}, l: {}, r: {}".format(a[j+1:r+1], j+1, r+1))
    print("")
    randomized_quick_sort2(a, l, j-1)
    randomized_quick_sort2(a, j+1, r)
    return a
    # recursively sort the left and right halves until either null or len(1) arrays are returned


def randomized_quick_sort3(a, l, r):
    print("a: {}, l: {}, r: {}".format(a, l, r))
    if l >= r:  # null
        return
    k = random.randint(l, r)  # pick a random index to be the pivot
    a[l], a[k] = a[k], a[l]  # switch a[l] and a[k] bc l is the pivot in partitions
    #use partition3
    print("k = {}, a = {}".format(k, a))
    j_start, j_end = partition3(a, l, r)  # find the partition point for the random index
    print("k = {}, m = {}, a: {}".format(k, j_start, j_end, a))
    print("Left Half: {}, l: {}, r: {}".format(a[l:j_start], l, j_start))
    print("Middle:{}", a[j_start:j_end])
    print("Right Half: {}, l: {}, r: {}".format(a[j_end:r+1], j_end, r+1))
    print("")
    randomized_quick_sort3(a, l, j_start-1)
    randomized_quick_sort3(a, j_end, r)
    return a
    # recursively sort the left and right halves until either null or len(1) arrays are returned


def test_partition():
    j3, j_end = partition3([2, 2, 2, 3, 5, 1, 3, 0], l=0, r=7 )
    assert j3 == 2, j3
    assert j_end == 5, j_end

    # j2 = partition2([2, 2, 2, 3, 5, 1, 3, 0],l=0,r=7)
    # assert  j2 == 4, j2
    # assert a2 == [0, 2, 2, 1, 2, 3, 3, 5], a2


def test_qs():
    qs_test = randomized_quick_sort2([19, 20, 10, 30], 0, 3)
    assert qs_test == [10, 19, 20, 30], qs_test

    qs_test2 = randomized_quick_sort2([2, 3, 9, 2, 2], 0, 4)
    assert qs_test2 == [2, 2, 2, 3, 9], qs_test2

    # qs_test3 = randomized_quick_sort3([2, 3, 9, 2, 2], 0, 4)
    # assert qs_test3 == [2, 2, 2, 3, 9], qs_test3



if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    test_partition()
    test_qs()
