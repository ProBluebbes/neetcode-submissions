class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        
        A = nums1 if l1 <= l2 else nums2
        B = nums2 if l1 <= l2 else nums1

        l = 0
        r = len(A) - 1
        half = len(A+B)//2
        
        while True:
            i = l + (r-l)//2
            j = half-i-2

            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i+1] if len(A) - 1 > i else float("infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j+1] if len(B) - 1 > j else float("infinity")

            if A_left > B_right:
                r = i - 1
                continue
            
            if B_left > A_right:
                l = i + 1
                continue

            if (l1 + l2) % 2 == 0:
                return (max(A_left, B_left)+min(A_right, B_right))/2
            else:
                if i + 1 > len(A) - 1:
                    return B[j+1]

                if j + 1 > len(B) - 1:
                    return A[i+1]

                return min(A[i+1], B[j+1])
