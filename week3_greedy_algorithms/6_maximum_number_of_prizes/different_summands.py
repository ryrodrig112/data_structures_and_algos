# Uses python3
import sys

def optimal_summands(n):
    summands = []
    candies_left = n
    prize = 0
    while candies_left:
        prize += 1
        candies_left -= prize
        if candies_left <= prize:
            prize += candies_left
            candies_left = 0
        summands.append(prize)
    return summands


def test_algo():
    assert optimal_summands(2) == [2], optimal_summands(2)
    assert optimal_summands(6) == [1, 2, 3], optimal_summands(6)
    assert optimal_summands(8) == [1, 2, 5], optimal_summands(8)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # summands = optimal_summands(n)
    # print(len(summands))
    # for x in summands:
    #     print(x, end=' ')
    test_algo()
