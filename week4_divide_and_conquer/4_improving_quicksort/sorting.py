# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    j_len = 1
    for i in range(l+1, r+1):
        if a[i] < x:
            # remove a[i] from current location and put at beginning
            # increment j
            tmp = a[i]
            del a[i]
            a.insert(l, tmp)
            j += 1
            print(a)
        elif a[i] == x:
            # remove item from current location and put it at jth location
            tmp = a[i]
            del a[i]
            a.insert(j, tmp)
            j_len += 1
            print(a)
        else:
            pass
    # a.insert(j, a[l])
    j_end = j + j_len
    print(a)
    print(a[j:j_end])
    return j, j_end


def partition2(nums, l, r):
    x = nums[l]  # pivot value
    j = l  # initial pivot location
    for i in range(l + 1, r + 1):
        if nums[i] <= x:
            j += 1  # move pivot to the right
            nums[i], nums[j] = nums[j], nums[i]  # swap ith element with pivot
        print(nums[i], nums)
    nums[l], nums[j] = nums[j], nums[l] # put a [l] into the pivot location
    print(nums)
    return j


def randomized_quick_sort2(a, l, r):
    print("a: {}, l: {}, r: {}".format(a, l, r))
    if l >= r:  # null
        return
    k = random.randint(l, r)  # pick a random index to be the pivot
    a[l], a[k] = a[k], a[l]  # switch a[l] and a[k] bc l is the pivot in partitions
    #use partition3
    print("k = {}, a = {}, r = {}".format(k, a, r))
    j = partition2(a, l, r)  # find the partition point for the random index
    print("k = {}, m = {}, a: {}, r: {}".format(k, j, a, r))
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
    # j3, j_end = partition3([2, 2, 2, 3, 5, 1, 3, 0], l=0, r=7 )
    # assert j3 == 2, j3
    # assert j_end == 5, j_end

    partition3([2, 2, 2, 3, 9], 0, 4)

    # j2 = partition2([2, 2, 2, 3, 5, 1, 3, 0],l=0,r=7)
    # assert  j2 == 4, j2


def test_qs():
    # qs_test = randomized_quick_sort2([19, 20, 10, 30], 0, 3)
    # assert qs_test == [10, 19, 20, 30], qs_test
    #
    # qs_test2 = randomized_quick_sort2([2, 3, 9, 2, 2], 0, 4)
    # assert qs_test2 == [2, 2, 2, 3, 9], qs_test2

    qs_test3 = randomized_quick_sort3([2, 3, 9, 2, 2], 0, 4)
    assert qs_test3 == [2, 2, 2, 3, 9], qs_test3



if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    # test_partition()
    test_qs()
