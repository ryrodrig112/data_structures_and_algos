# Uses python3
import sys

def get_change(m):
    num_10s = m // 10
    num_5s = m % 10
    num_1s = m % 5
    return num_10s + num_5s + num_1s


def test_algo():
    assert get_change(2), "Given example, returned {}".format(get_change(2))
    assert get_change(28), "Given example, returned {}".format(get_change(6))

if __name__ == '__main__':
    test_algo()
    # m = int(sys.stdin.read())
    # print(get_change(m))
