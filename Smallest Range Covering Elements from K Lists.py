import heapq
class Solution:
    def smallestRange(self, num: list[list[int]])->list[int]:
        min_heap = []
        max_val = float('-inf')
        for i in range(len(int)):
            heapq.heappush(min_heap,(num[i][0],i,0))
            max_val = max(max_val,num[i][0])
        result_range = [-float('inf'),float('inf')]
        while min_heap:
            min_val,list_idx,elem_idx = heapq.heappop(min_heap)
            if max_val - min_val <result_range[1] - result_range[0]:
                result_range = [min_val,max_val]
            if elem_idx + 1 == len(int[list_idx]):
                break
            next_val = num[list_idx][elem_idx + 1]
            heapq.heappush(min_heap,(next_val, list_idx,elem_idx + 1))
            max_val = max(max_val, next_val)
        return result_range