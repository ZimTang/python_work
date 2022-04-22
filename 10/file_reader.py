with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # 在这个文件中，每行的末尾都有一个看不见的换行符
    for line in file_object:
        print(line)

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)



# print(contents)
#
# with open('../01/hello_world.py') as demo:
#     content = demo.read()
#
# print(content)
