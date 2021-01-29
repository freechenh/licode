from copy import deepcopy

stock_cost_elements = {'R': '/', 'F': '\\', 'C': '_'}

axis = {'Y': '|', 'X': '-'}

stock_data = '''
3
RCRFCRFFCCRRC
CFF
FFFCCRRCCCRR'''


# print("")

def judge_is_exist_stock_cost(index, stock_cost):
    if stock_cost[index]:
        return stock_cost
    



def judge_max_fall(stock_cost_element):
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
            stock_cost.insert(x, deepcopy(base_stock_cost))
            stock_cost[x][y + 1] = stock_cost_elements[i]
            last_location = (x, y + 1)
        elif i == 'F' and last_element in ('C', 'F'):
            if x
            stock_cost.insert(x, deepcopy(base_stock_cost))
            stock_cost[x][y + 1] = stock_cost_elements[i]
            last_location = (x, y + 1)
            pass
        else:
            pass
    for i in stock_cost:
        print(i)


judge_max_fall('RC')

# def stock_trends_chart(stock_cost_element):
#     print('''|\n|\n|''')
#     print('+------------')
#     print(r'''
#     |             _
#     |  _/\_/\    /
#     | /      \__/
#     +--------------''')
#     print(r'''
#         |             _
#         |  _/\_/\    /
#         | /      \__/
#         +--------------''')
#     pass

# for i in range(1, 4):
#     print("Case #%s:" % i)
#     stock_trends_chart(stock_data)
#     print("\n")
