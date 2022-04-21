favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name in favorite_languages.keys():
    print(name.title())

for language in favorite_languages.values():
    print(language.title())

# 通过对包含重复元素的列表调用 set()，可让 Python 找出列表中独一无二的元素，并使用这
# 些元素来创建一个集合。
for language in set(favorite_languages.values()):
    print(language.title())