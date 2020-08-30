def isBadVersion(index):
    if index in (2, 3):
        return True


class Solution:
    @staticmethod
    def first_bad_version(n):
        start = 1
        end = n
        while start < end:
            index = start + (end - start) // 2
            if isBadVersion(index):
                end = index
            else:
                start = index + 1
        return end


if __name__ == '__main__':
    demo = Solution()
    print(demo.first_bad_version(5))
