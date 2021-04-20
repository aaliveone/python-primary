alien_0 = {'color': 'green'}
print("The alien is {}.".format(alien_0['color']))

alien_0['color']='yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

print("Original x-position: " + str(alien_0['x_position']))

#向右移动外星人
#根据外星人当前速度决定将移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的速度一定很快
    x_increment = 3

#新位置=老位置+增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New-position: " + str(alien_0['x_position']))