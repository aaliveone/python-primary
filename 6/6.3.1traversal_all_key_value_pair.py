user_0 = {
    'username': 'eferai',
    'first': 'enrico',
    'last': 'ferai',
    }

for key, value in user_0.items():#for语句value1,value2;items()遍历键值对
    print("\nKey: " + key)
    print("Value: " + value)

#遍历键值对
favorite_language={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pyton',
    }

for name,language in favorite_language.items():#items()遍历键值对
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

friends = ['jen', 'jack', 'sarah', 'genshin', 'edward', 'qing', 'phil']

for name_1 in friends:
    if name_1 in favorite_language:
        print("Hi " +name_1.title() + ", thanks for you!")
    else:
        print("Hi " + name_1.title() + ", can you help me?")