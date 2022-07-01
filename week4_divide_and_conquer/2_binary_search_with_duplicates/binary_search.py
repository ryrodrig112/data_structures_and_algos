def binary_search(keys, query):
    # write your code here
    indices = []

    for item in query:
        low = 0
        high = len(keys)
        while high > low:
            keys_i = keys[low:high]
            mid = len(keys_i)//2
            print(item, low, high, mid, keys_i)
            if item == keys_i[mid]:
                if len(keys_i) == 1:
                    indices.append(mid + low)
                    break
                elif keys_i[mid] != keys_i[mid-1]:
                    indices.append(mid + low)
                    break
                else:
                    high = mid
            elif item > keys_i[mid]:
                low += mid + 1
            elif item < keys_i[mid]:
                high = mid
        if high <= low:
            indices.append(-1)
    return indices


def test_algo():
    assert binary_search([1, 1, 1, 3], [1]) == [0], binary_search([1, 1, 3], [1])
    assert binary_search([2, 4, 4, 4, 7, 7, 9], [9, 4, 5, 2]) == [6, 1, -1, 0], \
        binary_search([2, 4, 4, 4, 7, 7, 9], [9, 4, 5, 2])

if __name__ == '__main__':
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
    test_algo()
