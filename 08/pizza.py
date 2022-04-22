# 结合使用位置实参和任意数量实参
def make_pizza(size, *pizzas):
    for pizza in pizzas:
        print(pizza)
    print(size)


# make_pizza(10, 'curry', 'james')
