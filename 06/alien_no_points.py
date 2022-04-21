alien_0 = {'color': 'green', 'speed': 'slow'}
# 如果指定的键有可能不存在，应考虑使用方法 get()，而不要使用方括号表示法
point_value1 = alien_0.get('points','no point value assigned')
point_value2 = alien_0.get('points')

print(point_value1)
print(point_value2)

