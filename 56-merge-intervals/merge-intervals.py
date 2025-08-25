class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  

        # Sort the intervals by start time using the lambda function and the start time as the key
        intervals.sort(key=lambda interval : interval[0])
        solution = [intervals[0]]

        for start, end in intervals[1:]:
            previousEndTime = solution[-1][1]

            # Check if the start of the second interval is within the range of the first, if so, update with the max of the end intervals
            if start <= previousEndTime:
                solution[-1][1] = max(end, previousEndTime)

            # If it isn't, start a new interval
            else:
                solution.append([start,end])

        return solution