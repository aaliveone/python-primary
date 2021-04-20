#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30): #range(30)创建0-29这30个数
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print("\nTotal number of aliens: " + str(len(aliens)))
print("\nTotal number of aliens: {}.".format(len(aliens)))