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
    return j, j_len


def partition2(a, l, r):
    x = a[l]  # pivot value
    j = l  # initial pivot location
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1  # move pivot to the right
            a[i], a[j] = a[j], a[i]  # swap ith element with pivot
    a[l], a[j] = a[j], a[l] # put a [l] into the pivot location
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:  # if the array is null
        return
    k = random.randint(l, r)  # pick a random index to be the pivot
    a[l], a[k] = a[k], a[l]  # switch a[l] and a[k] bc l is the pivot in partitions
    #use partition3
    m = partition2(a, l, r)  # find the partition point
    randomized_quick_sort(a, l, m - 1);  # recursively sort the left half
    randomized_quick_sort(a, m + 1, r);  # recursively sort the right half


def test_partition():
    j3, j_len = partition3([2, 2, 2, 3, 5, 1, 3, 0], l=0, r=7 )
    assert j3 == 2, j3
    assert j_len == 3, j_len

    j2 = partition2([2, 2, 2, 3, 5, 1, 3, 0],l=0,r=7)
    assert  j2 == 4, j2


def test_qs():
    qs_test = randomized_quick_sort([2, 3, 9, 2, 2], 0, 4)
    assert  qs_test== [2,2,2,3, 9], qs_test




if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    test_partition()
    test_qs()
