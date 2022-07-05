# Uses python3
import sys
import math
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    j_len = 1
    for i in range(l + 1, r + 1):
        if a[i] < x:
            # remove a[i] from current location and put at beginning
            # increment j
            tmp = a[i]
            del a[i]
            a.insert(l, tmp)
            j += 1
        elif a[i] == x:
            # remove item from current location and put it at jth location
            tmp = a[i]
            del a[i]
            a.insert(j, tmp)
            j_len += 1
        else:
            pass
    # a.insert(j, a[l])
    j_end = j + j_len
    return j, j_end


def randomized_quick_sort3(a, l, r):
    if l >= r:  # null
        return
    k = random.randint(l, r)  # pick a random index to be the pivot
    a[l], a[k] = a[k], a[l]  # switch a[l] and a[k] bc l is the pivot in partitions
    # use partition3
    j_start, j_end = partition3(a, l, r)  # find the partition point for the random index
    randomized_quick_sort3(a, l, j_start - 1)
    randomized_quick_sort3(a, j_end, r)
    return a


def minimum_distance(x, y):
    x1 = x.copy()
    def get_distance(a, b):
        distance = (((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)) ** .5
        return distance

    def get_median(a):
        mid = len(a) / 2
        if len(a) % 2 == 0:
            return (a[int(mid - 1)] + a[int(mid)]) / 2
        else:
            return a[int(mid - .5)]

    if len(x) <= 3:
        min_dist = -1
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                tmp_dist = get_distance([x[i], y[i]], [x[j], y[j]])
                print("test")
                if min_dist < 1:
                    min_dist = tmp_dist
                else:
                    if tmp_dist < min_dist:
                        min_dist = tmp_dist
        return min_dist

    # get median point of y to create vertical
    # sort y, get one of len // 2 position
    sorted_x = randomized_quick_sort3(x1, 0, len(x) - 1)
    median_x = get_median(sorted_x)

    # left_half  =  check sizes on left half
    # right_half = check sizes on right half
    fil_half = [i <= median_x for i in x]

    left_half_x = [item for i, item in enumerate(x) if fil_half[i]]
    left_half_y = [item for i, item in enumerate(y) if fil_half[i]]
    right_half_x = [item for i, item in enumerate(x) if not fil_half[i]]
    right_half_y = [item for i, item in enumerate(y) if not fil_half[i]]
    left_half = minimum_distance(left_half_x, left_half_y)
    right_half = minimum_distance(right_half_x, right_half_y)
    min_dist = min(left_half, right_half)

    fil_dist = [abs(point - median_x) < min_dist for point in x]
    x_close = [item for i, item in enumerate(x) if fil_dist[i]]
    y_close = [item for i, item in enumerate(y) if fil_dist[i]]
    if len(x_close) >= 2:
        for i in range(len(x_close) - 1):
            for j in range(i + 1, len(x_close)):
                print("test")
                tmp_dist = get_distance([x_close[i], y_close[i]], [x_close[j], y_close[j]])
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
    return min_dist

def test_algo():
    # tc1 = minimum_distance([0, 3], [0, 4])
    # assert tc1 == 5, tc1

    # tc2 = minimum_distance([7, 1, 4, 7], [7, 100, 8, 7])
    # assert tc2 == 0, tc2
    #
    tc3 = minimum_distance([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4])
    assert tc3 == 2**.5, tc3

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    # print("{0:.9f}".format(minimum_distance(x, y)))
    test_algo()