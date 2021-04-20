users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'prinxction',
        },
    'mcuie': {
        'first': 'marie',
        'last': 'cuise',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    lacation = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + lacation.title())