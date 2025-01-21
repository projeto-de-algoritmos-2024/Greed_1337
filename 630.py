class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key=lambda x: x[1])
        
        maxHeap = []
        total_time = 0
        
        for i in range(len(courses)):
            duration, deadline = courses[i]
            total_time += duration
            heapq.heappush(maxHeap, -1*courses[i][0])
            
   
            if total_time > deadline:
                longest = -1 * heapq.heappop(maxHeap)
                total_time -= longest
        
        return len(maxHeap)