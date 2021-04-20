favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):#sorted()顺序遍历键值
    print(name.title() + ", thank you for taking the poll.")