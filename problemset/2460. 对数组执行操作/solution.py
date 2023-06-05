class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 执行n-1步操作
        for i in range(len(nums) - 1):
            # 如果当前元素和下一个元素相等
            if nums[i] == nums[i + 1]:
                # 当前元素变为原来的2倍
                nums[i] *= 2
                # 下一个元素变为0
                nums[i + 1] = 0

        # 将所有的0移动到数组的末尾
        nums = [x for x in nums if x != 0] + [0] * nums.count(0)

        return nums