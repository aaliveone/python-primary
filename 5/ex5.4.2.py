current_users=['kONG', 'ying', 'paimeng', 'wendi', 'zhongli']

new_users=['Kong', 'ying', 'qing', 'xiao', 'xiangling']

cus=[]
for current_user in current_users:
    cus.append(current_user.lower())

for new_user in new_users:
    new_u = new_user.lower()
    if new_u in cus:
        print("Please")
    else:
        print("OK")