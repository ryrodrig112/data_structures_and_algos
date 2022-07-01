# Uses python3
import sys
import time

def get_majority_element(a, left=None, right=None):
    dict_tracker = {}
    for i in a:
        dict_tracker[i] = 0
    for i in a:
        dict_tracker[i] += 1
    for key in dict_tracker:
        if dict_tracker[key] > (len(a) / 2):
            return key
    return -1


def test_algo():
    assert get_majority_element([2, 3, 2, 9, 2]) == 2, get_majority_element([2, 3, 2, 9, 2])
    assert get_majority_element([1, 2, 3, 4, 5]) == -1, get_majority_element([1, 2, 3, 4, 5])
    assert get_majority_element([1, 3, 2, 1, 2]) == -1, get_majority_element([1, 3, 2, 1, 2])

    t0 = time.process_time()
    a = [i for i in range(10**5)]
    get_majority_element(a)
    t1 = time.process_time()
    assert time.process_time() < 1, t1-t0


if __name__ == '__main__':
    # test_algo()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
