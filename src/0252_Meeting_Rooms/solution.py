from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals == []:
            return True
        intervals.sort()
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < intervals[idx - 1][1]:
                return False
        return True
