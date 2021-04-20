players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])#切片索引

print(players[1:4])#与函数range()一样， Python在到达你指定的第二个索引前面的元素后停止

print(players[:4])#由于没有指定起始索引， Python从列表开头开始提取

print(players[2:])#提取从第3个元素到列表末尾的所有元素

print(players[-3:])#输出列表中最后三个值

print(players[:-1])#输出列表中除最后一个元素的所有元素

print(players[:])#创建列表副本