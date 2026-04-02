class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        max_length = 0
        for i in freq:
            if i + 1 in freq:
                max_length = max(max_length, freq[i] + freq[i + 1])

        return max_length
