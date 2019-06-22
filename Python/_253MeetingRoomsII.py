"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # intervals.sort(lambda a,b: a[0]-b[0])
        # intervals.sort(lambda a,b: a.start-b.start)
        so = sorted(intervals, key=(lambda x:x.start))

        rooms = {}
        # rooms[0] = so[0][1]
        rooms[0] = so[0].end
        for i,cur in enumerate(so[1:]):
            flag = 0 # default need new room
            for j,room in enumerate(rooms):
                # if cur[0] >= rooms[j]:
                if cur.start >= rooms[j]:
                    rooms[j] = cur.end
                    flag = 1
                    break
            if flag == 0:
                room_num = len(rooms)
                rooms[room_num] = cur.end

        return len(rooms)





        # Write your code here


intervals = [(0, 30), (5, 10), (15, 20)]
s = Solution()
r = s.minMeetingRooms(intervals)
print(r)
