favorite_places = {
    'xingqiu': ['wangmintang', 'chongyunjia',],
    'xiangling': ['wangmintang', 'tianqiugu',],
    'keli': ['wangfengshandi', 'guojiuhu', 'qingquanhu'],
    }

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places:")
    for place in places:
        print("\t" + place.title())