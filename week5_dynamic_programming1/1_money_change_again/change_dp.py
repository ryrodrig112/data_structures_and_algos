# Uses python3
import sys
import time


def get_change(m):
    # fill in the change tracker from left to right
    denominations = [1, 3, 4]
    change_tracker = {1:1, 3:1, 4:1,}
    for amount in range(1, m+1):
        if amount not in denominations:
            tests = []
            recursive_cases = [amount - denomination for denomination in denominations]
            for option in recursive_cases:
                if option > 0:
                    tests.append(change_tracker[option] + 1)
            change_tracker[amount] = min(tests)
    return change_tracker[m]


def test_algo():
    # for i in [1,3, 4]:
    #     assert get_change(i) ==1, "Failing base case"

    # tc1 = get_change(2)
    # assert tc1 == 2, tc1

    tc2 = get_change(34)
    assert tc2 == 9, tc2

    time1 = time.process_time()
    get_change(1000)
    time2 = time.process_time()
    time_dif = time2-time1
    assert time_dif < 1, time_dif



if __name__ == '__main__':
    # m = int(sys.stdin.read())
    # print(get_change(m))
    test_algo()
