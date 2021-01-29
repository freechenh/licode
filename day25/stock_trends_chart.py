from copy import deepcopy
from functools import reduce

stock_cost_elements = {'R': '/', 'F': '\\', 'C': '_'}

axis = {'Y': '|', 'X': '-'}

stock_data = '''

3
RCRFCRFFCCRRC
CFF
FFFCCRRCCCRR'''


def add_x_y(stock_cost_element, len_y):
    """给股票加上坐标轴"""
    y_axis = ['+'] + ['-'] * (len_y - 1)
    stock_cost_element.append(y_axis)
    for i in stock_cost_element[:-1]:
        i[0] = '|'
    return stock_cost_element


def judge_max_fall(stock_cost_element):
    """构造股票趋势图"""
    last_location = (0, 2)
    len_y = len(stock_cost_element) + 3
    base_stock_cost = [' '] * len_y
    stock_cost = [
        deepcopy(base_stock_cost)
    ]
    x, y = last_location
    stock_cost[x][y] = stock_cost_elements[stock_cost_element[0]]
    last_element = stock_cost_element[0]
    for i in stock_cost_element[1:]:
        x, y = last_location
        if last_element == 'R' and i in ('R', 'C'):
            if x == 0:
                stock_cost.insert(x, deepcopy(base_stock_cost))
                stock_cost[x][y + 1] = stock_cost_elements[i]
                last_location = (x, y + 1)
            else:
                stock_cost[x - 1][y + 1] = stock_cost_elements[i]
                last_location = (x - 1, y + 1)
        elif i == 'F' and last_element in ('C', 'F'):
            if x == len(stock_cost) - 1:
                stock_cost.append(deepcopy(base_stock_cost))
            stock_cost[x + 1][y + 1] = stock_cost_elements[i]
            last_location = (x + 1, y + 1)
        else:
            stock_cost[x][y + 1] = stock_cost_elements[i]
            last_location = (x, y + 1)
        last_element = i
    stock_cost = add_x_y(stock_cost, len_y)
    return stock_cost


def stock_trend_chart(stock_cost_element):
    """打印股票趋势图"""
    for i in stock_cost_element:
        data = reduce(lambda x, y: x + y, i)
        print(data)


def main(stock_cost_element):
    data_len, *data = stock_cost_element.strip('\n').split('\n')
    if int(data_len) != len(data):
        print('stock num is wrong')
    for i in range(len(data)):
        print("Case #%s:" % i)
        stock_trend_chart(judge_max_fall(data[i]))
        print("\n")


if __name__ == '__main__':
    main(stock_data)
