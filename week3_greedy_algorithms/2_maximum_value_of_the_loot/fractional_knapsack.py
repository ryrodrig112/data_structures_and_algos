# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    #  1. Is there any room left? If not, we're done
    #  2. Find the most valuable item per weight, and take as much as possible
    #  2a. Dictionary {index : [value, weight, weight / lb], ...  }
    #
    if capacity == 0:
        return 0
    else:
        value_per_weight = [values[i] / weights[i] for i in range(len(weights))]
        argmax = lambda i: value_per_weight[i]
        idx_most_valuable = max(range(len(value_per_weight)), key=argmax)
        if weights[idx_most_valuable] < capacity:
            # remove capacity
            # take all of item
            # remove item from list
            capacity -= weights[idx_most_valuable]
            value = values[idx_most_valuable]
            del values[idx_most_valuable]
            del weights[idx_most_valuable]
        elif weights[idx_most_valuable] >= capacity:
            # take capacity
            value = capacity * value_per_weight[idx_most_valuable]
            capacity = 0

    return value + get_optimal_value(capacity, weights, values)


def test_algo():
    assert get_optimal_value(50, [20, 50, 30], [60, 100, 120]) == 180, "Given Example, returned {}" \
        .format(get_optimal_value(50, [20, 50, 30], [60, 100, 50]))
    assert get_optimal_value(10, [500], [30]) == 166.6667, "Given Example, returned {}" \
        .format(get_optimal_value(10, [30], [500]))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    # test_algo()
