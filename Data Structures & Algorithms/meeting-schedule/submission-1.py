"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        prev_end, curr_start = 0, 0 
        for meeting in intervals:
            curr_start = meeting.start
            if curr_start < prev_end:
                return False
            prev_end = meeting.end
        return True
