my_friends = []
friend_1 = {
    'first': 'yanran',
    'last_name': 'murong',
    'age': 18,
    'city': 'wuhu',
    }

print("Her first name is " + friend_1['first'].title() + ".")
print("Her last name is " + friend_1['last_name'].title() + ".")
print("She is " + str(friend_1['age']) + " years old.")
print("Now, she live in " + friend_1['city'] + ".")

like_number={'xiangling': 12, 'chongyun': 3, 'zhongli': 5, 'keqing': 7, 'ningguang': 8}
print("1 like " + str(like_number['xiangling']) + ".")
print("chong yun like " + str(like_number['chongyun']) + ".")
print("3 like " + str(like_number['zhongli']) + ".")

friend_2 = {
    'first': 'xianggang',
    'last_name': 'li',
    'age': 23,
    'city': 'tianjin',
    }
friend_3 = {
    'first': 'zhuanghu',
    'last_name': 'sun',
    'age': 23,
    'city': 'shenyang',
    }

my_friends.append(friend_1)
my_friends.append(friend_2)
my_friends.append(friend_3)

a=1
for friend in my_friends:

    print("\n" + str(a) +"st full name: "
          + friend['first'] + " "
          +friend['last_name'] + ".")
    a += 1
    print("\t" + friend['first'] + " is "
          + str(friend['age']) + " years old.")
    print("\tNow, " + friend['first'] + " live in "
          +friend['city'].title() + ".")

    print(friend)