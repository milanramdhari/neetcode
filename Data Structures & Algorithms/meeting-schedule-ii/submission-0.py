"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0 
        
        intervals.sort(key = lambda interval : interval.start)
        days = []

        for meeting in intervals:
            curr_start = meeting.start
            placed = False
            for day in days:
                if day[-1].end <= curr_start:
                    day.append(meeting)
                    placed = True
                    break

            if not placed:   
                new_day = [meeting]
                days.append(new_day)
        
        return len(days)

# intervals = [(0,40),(5,10),(15,20)]
# days = [[(0, 0), (0, 40)], [(5, 10), (15, 20)]]
# curr_start = 15
# 


        