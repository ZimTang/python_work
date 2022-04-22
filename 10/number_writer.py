import json

nums = [2, 3, 4]

filename = 'number.json'

with open(filename, 'w') as f:
    json.dump(nums, f)

with open(filename) as f:
    content = json.load(f)

print(content)
