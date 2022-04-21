bicycles = ['trek','cannodale','redline']

print(bicycles[0].title())
# 返回最后一个
print(bicycles[-1])

motorcycles = ['honda','suzuki','yamaha']
motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素到末端
motorcycles.append('ducati')

# 指定位置添加元素
motorcycles.insert(0,'demo')
print(motorcycles)

# del删除元素
del motorcycles[1]

# pop尾部删除元素 并返回该元素
motorcycles.pop()

# 指定删除元素
motorcycles.pop(1)

# 根据值删除元素 只删除第一个指定的值
motorcycles.remove('suzuki')

