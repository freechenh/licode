# 力扣练习
## 第一天 重复的字符串
- 确定一个字符串是否是由重复的子串构成
    - 使用的是KMP算法，但是没看懂，还得再看看
    - 可以使用枚举来暴力破解
## 第二天 递增的子序列
- 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
    - 
## 第三天 算法图解
- 大O表示法   O(n)  表示运行时间，n表示操作的次数
    - 常见的运行时间 
        - O (log n )，也叫对数时间 ，这样的算法包括二分查找
        - O (n )，也叫线性时间 ，这样的算法包括简单查找。
        - O (n * log n )，这样的算法包括第4章将介绍的快速排序——一种速 度较快的排序算法。
        - O (n 2 )，这样的算法包括第2章将介绍的选择排序——一种速度较 慢的排序算法。
        - O (n !)，这样的算法包括接下来将介绍的旅行商问题的解决方案 ——一种非常慢的算法。

- 二分法
```python
def binary_search(list_, item_):
    low = 0
    high = len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item_:
            return mid
        if guess > item_:
            high = mid - 1
        if guess < item_:
            low = mid + 1
    return None
```

## 第四天 算法图解
- 