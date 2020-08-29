

class Solution:
    @staticmethod
    def my_sqrt(x):
        start, end = 0, x
        # end = x
        if x == 1:
            return 1
        while end - start != 1:
            sqrt_result = (start + end) // 2
            if sqrt_result**2 == x:
                return sqrt_result
            if sqrt_result**2 > x:
                end = sqrt_result
            else:
                start = sqrt_result
        return start


if __name__ == '__main__':
    demo = Solution()
    print(demo.my_sqrt(1))
