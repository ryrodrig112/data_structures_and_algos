def binary_search(keys, query):
    # write your code here
    indices = []
    for item in query:
        low = 0
        high = len(keys)
        while high > low:
            keys = keys[low:high]
            mid = (high + low)//2 # mid = 2
            if item == keys[mid]: #  keys[mid] == 3
                indices.append(mid + low)
                break
            elif item > keys[mid]:
                low = mid + 1
            elif item < keys[mid]:
                high = mid
        if high <= low:
            indices.append(-1)
    return indices


def test_algo():
    assert binary_search([1, 2, 3, 4, 5] , [2]) == [1], binary_search([1,2,3,4,5,], [2])
    assert binary_search([1, 5, 8, 12, 13], [8, 1, 23, 1, 11]) == [2, 0, -1, 0, -1], binary_search([1,5,8,12,13,], [8, 1, 23, 1, 11])

if __name__ == '__main__':
    test_algo()
    # num_keys = int(input())
    # input_keys = list(map(int, input().split()))
    # assert len(input_keys) == num_keys
    #
    # num_queries = int(input())
    # input_queries = list(map(int, input().split()))
    # assert len(input_queries) == num_queries
    #
    # for q in input_queries:

    #     print(binary_search(input_keys, q), end=' ')
