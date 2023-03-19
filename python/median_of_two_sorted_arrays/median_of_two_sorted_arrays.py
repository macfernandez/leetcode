from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        sum_length = len1 + len2
        longest = len1 if len1 > len2 else len2
        if sum_length % 2:
            candidate_pos = sum_length//2
            for i in range(longest+1):
                if bool(nums1) and bool(nums2):
                    if nums1[0] <= nums2[0]:
                        if i == candidate_pos:
                            median = nums1[0]
                            break
                        nums1.pop(0)
                    else:
                        if i == candidate_pos:
                            median = nums2[0]
                            break
                        nums2.pop(0)
                else:
                    remain = nums1 if bool(nums1) else nums2
                    if i == candidate_pos:
                        median = remain[0]
                        break
                    remain.pop(0)
        else:
            candidates = list()
            candidate_m = sum_length//2 - 1
            candidate_n = candidate_m + 1
            for i in range(longest+1):
                if bool(nums1) and bool(nums2):
                    if nums1[0] <= nums2[0]:
                        if i == candidate_m:
                            candidates.append(nums1[0])
                        if i == candidate_n:
                            candidates.append(nums1[0])
                            break
                        nums1.pop(0)
                    else:
                        if i == candidate_m:
                            candidates.append(nums2[0])
                        if i == candidate_n:
                            candidates.append(nums2[0])
                            break
                        nums2.pop(0)
                else:
                    remain = nums1 if bool(nums1) else nums2
                    if i == candidate_m:
                        candidates.append(remain[0])
                    if i == candidate_n:
                        candidates.append(remain[0])
                        break
                    remain.pop(0)
            median = sum(candidates) / 2
        return median

#Solution().findMedianSortedArrays([1,2], [3])
#print('==========')
#Solution().findMedianSortedArrays([1,3], [2])
#print('==========')
#Solution().findMedianSortedArrays([1,3], [2,4])
#print('==========')
#Solution().findMedianSortedArrays([1,2,5,6], [3,4])
#print('==========')
#Solution().findMedianSortedArrays([1,2], [3,4])
