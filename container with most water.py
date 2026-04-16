class Solution:
    def maxArea(self, height: List[int]) -> int:
        r=len(height)-1
        l=0
        max_=0
        while l<r:
            min_=min(height[l],height[r])
            area=(r-l)*min_
            max_=max(max_,area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_
