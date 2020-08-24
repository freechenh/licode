

"""
重复的子字符串
"""


class Solution:
    @staticmethod
    def repeated_sub_string_pattern(s):
        n = len(s)
        if n > 10000:
            return False
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                result = list()
                for j in range(i, n):
                    a = s[j]
                    b = s[j - i]
                    if a == b:
                        result.append(True)
                    else:
                        result.append(False)
                if all(result):
                    """all()方法，入参是一个iterable如果iterable的所有元素不为0、''、False或者iterable为空，
                    all(iterable)返回True，否则返回False；
                    注意：空元组、空列表返回值为True，这里要特别注意。
                    >>> all([])             # 空列表
                    True
                    >>> all(())             # 空元组
                    True"""
                    return True
        return False


if __name__ == '__main__':
    demo = Solution()
    print(demo.repeated_sub_string_pattern("abab"))
