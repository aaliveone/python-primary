cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))#对列表进行临时排序;也可向函数sorted()传递参数reverse=True

print("\nHere is the original list again:")
print(cars)