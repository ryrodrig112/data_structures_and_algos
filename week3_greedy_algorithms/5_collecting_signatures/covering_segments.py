# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # write your code here
    #  1. Find left most segment
    while segments:
        segment_starts = [x[0] for x in segments]
        leftmost_point = min(segment_starts)
        leftmost_segments = list(filter(lambda x: x[0] == leftmost_point, segments))
        #  2. If multiple segments with same start, find shortest and "select"
        segment_length = lambda x: x[1] - x[0]
        seg = min(leftmost_segments, key=segment_length)
        intersection_dict = {}  # {point, [number of intersections,[list of lines hit by point]]}
        for point in range(seg[0], seg[1] + 1):
            num_intersections = 0
            lines_intersected = []
            for line in segments:
                if point in range(line[0], line[1] + 1):
                    num_intersections += 1
                    lines_intersected.append(line)
                intersection_dict[point] = [num_intersections, lines_intersected]
        optimal_point = max(intersection_dict, key=lambda key: intersection_dict[key][0])
        points.append(optimal_point)
        for line in intersection_dict[optimal_point][1]:
            segments.remove(line)
        # print(intersection_dict)
    return points
    # select key(point) with largest value
    # how many other points does it connect to?


def test_algo():
    assert optimal_points([(1, 3), (2, 5), (3, 6)]) == [3], "Given Value, returned {}" \
        .format(optimal_points([(1, 3), (2, 5), (3, 6)]))
    assert len(optimal_points([(4, 7), (1, 3), (2, 5), (5, 6)])) == 2, "Given Value, returned {}" \
        .format(len(optimal_points([(4, 7), (1, 3), (2, 5), (5, 6)])))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
    # test_algo()
