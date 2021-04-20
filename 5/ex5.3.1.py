alien_colors=['green','yellow','red']

for alien_color in alien_colors:
    if alien_color=='green':
        print("Player get 5 point!")
    #else:
    elif alien_color=='yellow':
        print("Player get 10 point!")
    elif alien_color=='red':
        print("Player get 15 point!")
    if alien_color!='green':
        print("Player not shit green.")