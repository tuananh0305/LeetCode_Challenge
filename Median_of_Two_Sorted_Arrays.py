'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        len1 = len(nums1)
        len2 = len(nums2)
        merge_len = len1+len2
        merge_mid = (len1+len2)//2
        l, r = 0, len1-1
        if len1==0:
            if merge_len%2==0:
                return((nums2[merge_mid-1]+nums2[merge_mid])/2.0)
            else:
                return(nums2[merge_mid])    
        
        while True:
            mid_1 = (l+r)//2
            mid_2 = merge_mid-mid_1-2
            # print(mid_1, mid_2)
        
            if mid_1 < 0:
                A=-float('inf')
                B = nums1[mid_1+1]
            else:
                A = nums1[mid_1]
                if mid_1+1>=len1:
                    B=float('inf')
                else:
                    B = nums1[mid_1+1]
                
            if mid_2<0:
                C=-float('inf')
                D = nums2[mid_2+1]
            else:
                C = nums2[mid_2]
                if mid_2+1>=len2:
                    D=float('inf')
                else:
                    D = nums2[mid_2+1]
            
            
            #check_mid_position(mid_1, mid_2)
            if (A<=D) and (C<=B):
                if merge_len%2==0:
                    return((max(A,C)+min(B,D))/2.0)
                else:
                    return(min(B,D))
            elif A>D:
                r = mid_1 - 1
            elif C>B:
                l = mid_1 + 1