class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()
        merged = []

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
        

    

