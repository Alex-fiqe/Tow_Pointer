class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n=len(nums2)
        r=0
        for i in range(n):
            while(r<m and nums2[i]>nums1[r]):
                r+=1
             
            del nums1[-1]        
            nums1.insert(r,nums2[i])
            r+=1
            m+=1
