like_number={
    'xiangling': [12,4,2],
    'chongyun': [3,128],
    'zhongli': [5,328],
    'keqing': [7,648],
    'ningguang': [8,115,725],
    }

for name, numbers in like_number.items():
    print("\n" + name.title() + " like number:")
    for number in numbers:
        print("\t" + str(number))