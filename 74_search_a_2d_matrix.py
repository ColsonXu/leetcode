class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# Solution 1
#        nums = []
#        for lst in matrix:
#            nums.extend(lst)
#        
#        l = 0
#        r = len(nums)
#        
#        while l < r:
#            mid = (l + r) // 2
#            if nums[mid] == target:
#                return True
#            elif nums[mid] < target:
#                l = mid + 1
#            else:
#                r = mid
#        return False

# Solution 2
        m_l = 0
        m_r = len(matrix)
        lst = []
        
        while m_l < m_r:
            mid = (m_l + m_r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                lst = matrix[mid]
                break
            elif matrix[mid][0] > target:
                m_r = mid
            else:
                m_l = mid + 1
        
        l = 0
        r = len(lst)
        
        while l < r:
            mid = (l + r) // 2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                l = mid + 1
            else:
                r = mid
        return False
