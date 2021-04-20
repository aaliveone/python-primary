#formatted name
def get_formatted_name(first_name,second_name):
    """Return clean name.返回整洁的姓名。

    first name名；second name姓"""
    full_name=first_name+' '+second_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)