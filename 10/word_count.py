def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        # 静默失败
        pass
    else:
        words = contents.split()

    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


filename = 'demo.txt'
count_words(filename)
