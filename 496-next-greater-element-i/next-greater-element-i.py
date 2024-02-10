class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        st=[]
        for i in range(len(nums2)-1,-1,-1):
            while st and nums2[i]>st[-1]:
                st.pop()
            if not st:
                d[nums2[i]]=-1
            else:
                d[nums2[i]]=st[-1]
            st.append(nums2[i])
        ans=[]
        for i in range(len(nums1)):
            ans.append(d[nums1[i]])
        return ans
        