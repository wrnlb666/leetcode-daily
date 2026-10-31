class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 确保 nums1 是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m: int = len(nums1)
        n: int = len(nums2)
        total_left = (m + n + 1) // 2  # 左半部分应有的元素总数

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # nums1 的分割点
            j = total_left - i  # nums2 的分割点

            # 处理边界：分割线在数组两端时，用 -inf / +inf 代替不存在的元素
            left1 = -9999999 if i == 0 else nums1[i - 1]
            right1 = 9999999 if i == m else nums1[i]
            left2 = -9999999 if j == 0 else nums2[j - 1]
            right2 = 9999999 if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                # 找到了正确的分割线
                if (m + n) % 2 == 1:
                    return max(left1, left2)  # 奇数：左半部分最大值
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1  # nums1 左边太大，分割线左移
            else:
                left = i + 1  # nums2 左边太大，等价于 nums1 分割线右移


nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
