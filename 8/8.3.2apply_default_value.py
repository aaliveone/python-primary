#定义参数时，形参中的默认值放在最后
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return clean name.返回整洁姓名。

    让中间的的名赋值为空字符串，相当于设了一个默认值，让实参变成可选的"""
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

musician=get_formatted_name('jack','hands')
print(musician)

#位置实参要先于关键字实参
musician=get_formatted_name('joo','hhhhh',middle_name='lee')
print(musician)