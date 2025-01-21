class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        pairs = sorted(zip(growTime, plantTime), reverse=True)

        curr_plant_time = 0
        max_bloom_time = 0

        for grow, plant in pairs:
            curr_plant_time += plant
            max_bloom_time = max(max_bloom_time, curr_plant_time + grow)

        return max_bloom_time