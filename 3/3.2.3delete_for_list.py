motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]#知道要删除的元素在列表中的位置，可使用del语句
print(motorcycles)

motorcycles.insert(0,'honda')
poped_motorcycle=motorcycles.pop()#将元素从列表中删除，并接着使用它的值
                                  #方法pop()可删除列表末尾的元素，并让你能够接着使用它
                                  #列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素
print(motorcycles)
print(poped_motorcycle)

motorcycles.pop()
print(motorcycles)

motorcycles.append('suzuki')
first_motorcycle=motorcycles.pop(0)#在括号中指定要删除的元素的索引，可删除相应位置的元素
print('The first motorcycle I owned was a '+first_motorcycle+'.')
#pop()删除元素后还能使用它

motorcycles.insert(0,'honda')
motorcycles.insert(1,'yamaha')
motorcycles.append('sucati')
print(motorcycles)

motorcycles.remove('suzuki')#不知道删除的值的位置，知道要删除的元素的值，用remove（）
print(motorcycles)
