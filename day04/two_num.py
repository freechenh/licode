class Solution:
    @staticmethod
    def two_sum(numbers, target):
        if len(numbers) == 2:
            return 1, 2
        for i in range(1, len(numbers) + 1):
            start = numbers[i - 1]
            end = target - start
            left, right = i, len(numbers)
            while left != right:
                if end > numbers[right - 1]:
                    break
                index = (left + right) // 2
                if end == numbers[index]:
                    return i, index + 1
                if end > numbers[index]:
                    left = index
                else:
                    right = index


demo = Solution()
print(demo.two_sum([3, 24, 50, 79, 88, 150, 345], 200))
