class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  

        revised_meetings = [meetings[0]]
        for i in range(1, len(meetings)):

            prev = revised_meetings[-1]

            if prev[1] >= meetings[i][0]:
                new_interval = [prev[0], meetings[i][1]]
                revised_meetings[-1] = [prev[0], max(prev[1], meetings[i][1])]
            
            else:
                revised_meetings.append(meetings[i])

        for meeting in revised_meetings:
            days -= meeting[1] - meeting[0] + 1

        return days
