# python3
import sys


def compute_min_refills(distance, tank, stops):
    #  1. Can we 1 shot it? if so then no stops required
    #  2. We can't make it all the way, so where do we have to stop at?
    #  3. If nowhere to stop, -1
    #  4. Otherwise, current stop =
    # Go to that stop and subtra
    refills = 0
    current_stop = 0
    driving = True
    while driving:
        if tank + current_stop >= distance:
            return refills
        else:
            available_stops = list(filter(lambda stop: stop <= current_stop + tank, stops))
            if not available_stops:
                return  -1
            else:
                current_stop = max(available_stops)
                refills += 1
                stops = list(filter(lambda stop: stop > current_stop, stops))


def test_algo():
    assert compute_min_refills(950, 400, [200, 375, 550, 750]) == 2, "Given Example, returned {}"\
        .format(compute_min_refills(950, 400, [200, 375, 550, 750]))
    assert compute_min_refills(10, 3, [1, 2, 5, 9]) == -1, "Given Example, returned {}" \
        .format(compute_min_refills(10, 3, [1, 2, 5, 9]))
    assert compute_min_refills(200, 250, [100, 150]) == 0, "Given Example, returned {}" \
        .format(compute_min_refills(10, 3, [1, 2, 5, 9]))


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
