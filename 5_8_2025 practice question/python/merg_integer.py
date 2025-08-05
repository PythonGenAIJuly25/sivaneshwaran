def merge_intervals(intervals):

    if not intervals or len(intervals) == 1:
        return intervals

   
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  
            last[1] = max(last[1], current[1])  
        else:
            merged.append(current)

    return merged


tests = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[1,4],[2,3]], [[1,4]]),
    ([[1,2],[3,4],[5,6]], [[1,2],[3,4],[5,6]]),
    ([[1,4],[2,5],[3,6]], [[1,6]]),
    ([[6,7],[2,4],[5,9]], [[2,4],[5,9]]),
    ([[1,4]], [[1,4]]),
    ([[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]])
]


for i, (input_data, expected) in enumerate(tests, 1):
    result = merge_intervals(input_data)
    print(f"Test Case {i}:  Output: {result}")
