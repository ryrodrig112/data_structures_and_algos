# Uses python3
import sys


def get_change(m):
    # fill in the change tracker from left to right
    denominations = [1, 3, 4]
    change_tracker = {1: 1, 3: 1, 4: 1, }
    for amount in range(1, m + 1):
        if amount not in denominations:
            tests = []
            recursive_cases = [amount - denomination for denomination in denominations]
            for option in recursive_cases:
                if option > 0:
                    tests.append(change_tracker[option] + 1)
            change_tracker[amount] = min(tests)
    return change_tracker[m]


def optimal_sequence(n):
    calculation_tracker = {1: [0, [1]]}
    for i in range(2, n + 1):
        if i not in calculation_tracker:
            recursive_cases = {'i - 1': i -1,
                               'i / 2': ...,
                               'i / 3': ... }
            if i % 2 == 0:
                recursive_cases['i / 2'] = (i/2)
            else:
                recursive_cases['i / 2'] = -1
            if i % 3 == 0:
                recursive_cases['i / 3'] = (i/3)
            else:
                recursive_cases['i / 3'] = -1
            tests = {}
            for case in recursive_cases.values():
                if case > 0:
                    num_ops = calculation_tracker[case][0] + 1
                    tests[case] = num_ops
            min_key = min(tests, key = tests.get)
            sequence = calculation_tracker[min_key][1] + [i]
            min_ops = min(tests.values())
            calculation_tracker[i] = [min_ops, sequence]
    return calculation_tracker[n]


def test_algo():
    tc1 = optimal_sequence(9)
    assert tc1 == [2, [1,3,9]]

    tc2 = optimal_sequence(96234)
    print(tc2)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # sequence = list(optimal_sequence(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print(x, end=' ')
    test_algo()
