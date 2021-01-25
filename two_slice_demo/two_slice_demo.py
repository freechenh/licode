def xxx(list_, item):
    low = 0
    max_ = len(list_) - 1

    while low <= max_:
        index = (low + max_) // 2
        if list_[index] == item:
            return index
        elif list_[index] > item:
            max_ = index - 1
        else:
            low = index + 1


if __name__ == '__main__':
    list_ = [1, 3, 4, 5, 8, 10, 20, 22]
    print(xxx(list_, 1))
