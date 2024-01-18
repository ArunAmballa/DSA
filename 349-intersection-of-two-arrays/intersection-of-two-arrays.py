class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=[]
        i=0
        j=0
        last=-1
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j] and nums1[i]!=last:
                ans.append(nums1[i])
                last=nums1[i]
                i=i+1
                j=j+1
            else:
                if nums1[i]<nums2[j]:i=i+1
                else:j=j+1
        return ans

        