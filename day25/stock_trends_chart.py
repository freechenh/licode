stock_cost_elements = {'R': '/', 'F': '\\', 'C': '_'}

axis = {'Y': '|', 'X': '-'}

stock_data = '''
3
RCRFCRFFCCRRC
CFF
FFFCCRRCCCRR'''


# print("")

def stock_trends_chart(stock_cost_element):
    print('''|\n|\n|''')
    print('+------------')
    print(r'''
    |             _
    |  _/\_/\    /
    | /      \__/
    +--------------''')
    pass


for i in range(1, 4):
    print("Case #%s:" % i)
    stock_trends_chart(stock_data)
    print("\n")
