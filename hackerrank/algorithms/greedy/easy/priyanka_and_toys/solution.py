# Assume points come in sorted.. i.e. if not sorted sort them O(nlogn)
# This greedy algo works in O(n)
def pointsCoveredSorted(points):
    segments, i = [], 0
    n = len(points)
    while i < n:
        segment = [points[i], points[i] + 4]
        segments.append(segment)
        i += 1
        while i < n and points[i] <= segment[1]:
            i += 1
    return segments

n = int(raw_input())
weights = map(int, raw_input().split())
weights.sort() # O(nlogn)
print(len(pointsCoveredSorted(weights)))
