class Solution:
    @staticmethod
    def search(nums, target):
        start = 0
        end = len(nums)
        if target > nums[-1]:
            return -1
        while start <= end:
            index = (start + end) // 2
            if nums[index] == target:
                return index
            if nums[index] > target:
                end = index - 1
            else:
                start = index + 1
        return -1


if __name__ == '__main__':
    demo = Solution()
    print(demo.search([-1, 0, 3, 5, 9, 12], 13))
