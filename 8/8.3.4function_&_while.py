def get_formatted_name(first_name,second_name):
    """Return clean name.返回整洁的姓名。

    first name名；second name姓"""
    full_name=first_name+' '+second_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit!)")

    f_name=input("First name: ")
    if f_name=='q':
        break
    l_name=input("Last name: ")
    if l_name=='q':
        break
    format_name=get_formatted_name(f_name,l_name)
    print("\nHi, {}!".format(format_name))