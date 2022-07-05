import sys


def merge(l1, l2, inversion_tracker):
    num_inversions = sum(inversion_tracker)
    print("Merge b: {} and c: {}".format(l1,l2))
    d = []
    while l1 and l2:
        l1_1 = l1[0]
        l2_1 = l2[0]
        if l1_1 <= l2_1:
            d.append(l1_1)
            l1.pop(0)
        else:
            inversion_tracker[num_inversions] = 1
            print("Inversion, {} > {}! New tracker{}".format(l1_1, l2_1, inversion_tracker))
            d.append(l2_1)
            l2.pop(0)
    if l1:
        d += l1
    elif l2:
        d += l2
    print("d: {}".format(d))
    print("")
    return d, inversion_tracker


def merge_sort(a, b, left, right):
    print("a: {}, inversions: {}, left: {}, right: {}".format(a, b, left, right))
    array = a[left:right]
    print("array: {}".format(array))
    print("inversions so far: {}".format(sum(b)))
    if len(array) <= 1:
        return array, b
    m = (left + right)//2
    print("left half: {}". format(a[left:m]))
    print("right half: {}".format(a[m: right]))
    print("")
    l1, b = merge_sort(a, b, left, m)
    l2, b = merge_sort(a, b, m, right)

    a_prime, b = merge(l1, l2, b)
    return a_prime, b


def get_number_of_inversions(a, b, left, right):

    sorted_list, inversion_tracker = merge_sort(a, b, left, right)
    num_inversions = sum(inversion_tracker)
    return num_inversions


def test_algo():
    sorted_list, inversions = merge_sort([1, 3, 2, 4], [0, 0, 0, 0], 0, 4)
    assert sorted_list == [1,2,3,4], sorted_list

    tc1 = get_number_of_inversions([1, 3, 2, 4], [0, 0, 0, 0], 0, 4)
    assert tc1 == 1, tc1

    tc2= get_number_of_inversions([1, 3, 2, 1, 4], [0, 0, 0, 0], 0, 5)
    assert tc2 == 2, tc2

    tc3 = get_number_of_inversions([2,3,9,2,9], [0,0,0,0,0], 0, 5)
    assert tc3 == 2, tc3

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # print(n)
    # b = n * [0]
    # print(b)
    # print(get
    # _number_of_inversions(a, b, 0, len(a))
    test_algo()