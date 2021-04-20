favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

frinends = ['phil', 'sarah']
#for name in favorite_languages.keys():#keys()它返回一个列表，其中包含字典中的所有键
for name in favorite_languages:#遍历字典时，会默认遍历所有的键
    print(name.title())

    if name in frinends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")