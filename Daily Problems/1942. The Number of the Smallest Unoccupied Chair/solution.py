import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        times_with_index = [(times[i][0], times[i][1], i) for i in range(n)]
        times_with_index.sort(key=lambda x: x[0])

        available_chairs = list(range(n))
        heapq.heapify(available_chairs)

        occupied_chairs = []
        for arrival, leaving, friend in times_with_index:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                leave_time, chair_number = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair_number)

            assigned_chair = heapq.heappop(available_chairs)
            if friend == targetFriend:
                return assigned_chair
            
            heapq.heappush(occupied_chairs, (leaving, assigned_chair))