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


def fast_count_segments(starts, ends, points):
    #initialize way to keep track of segment intersections (not sorted)
    point_counter_dict = {point : None for point in points}

    # merge the lists together into a sorted one
    sorted_points = randomized_quick_sort3(starts + ends + points, 0, len(starts + ends + points) - 1)

    # if start, counter +=1
    # if end, counter += 0
    # if point, assign counter value to point

    counter = 0
    for point in sorted_points:
        if point in starts:
            counter +=1
        elif point in ends:
            counter -=1
        elif point in points:
            point_counter_dict[point] = counter
    return list(point_counter_dict.values())

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

def test_algo():
    tc1 = fast_count_segments([0, 7], [5, 10], [1,6,11])
    assert tc1 == [1, 0, 0], tc1

    tc2 = fast_count_segments([-10], [10], [-100, 100, 0])
    assert tc2 == [0, 0, 1], tc2

    tc3 = fast_count_segments([0, -3, 7], [5, 2, 10], [1, 6])
    assert tc3 == [2, 0]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends   = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    test_algo()

