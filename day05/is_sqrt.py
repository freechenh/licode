class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            x = left + (right - left) // 2
            data = x**2
            if data == num:
                return True
            if data > num:
                right = x - 1
            else:
                left = x + 1
        return False


if __name__ == '__main__':
    demo = Solution()
    print(demo.isPerfectSquare(17))
