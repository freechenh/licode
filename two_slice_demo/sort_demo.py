def xxxx(list_):
    min_ = list_[0]
    min_index = 0
    for i in range(0, len(list_)):
        if list_[i] <= min_:
            min_ = list_[i]
            min_index = i
    return min_, min_index


if __name__ == '__main__':
    list_x = [5, 43, 4, 8, 2, 1, 3]
    print(xxxx(list_x))
