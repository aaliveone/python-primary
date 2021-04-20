#user_names=['hangnu', 'admin', 'xingqiu', 'keli', 'mona']
user_names=[]

if user_names:
    for user_name in user_names:
        if user_name!='admin':
            print("Hello "+user_name.title()+", thank you for my help!")
        else:
            print("Hi "+user_name.title()+", welcome to Beijing!")
else:
    print("We need to find some users!")