class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for i, num in enumerate(nums):
          diff = target - num
          if diff in index_map:
              return [index_map[diff], i]
          index_map[num] = i
        return None