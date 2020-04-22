import sys
from VK_UserActivity import *

if __name__ == '__main__':
    with open('../config/config.json', 'r') as file:
        token = json.load(file)['vk_token']

    try:
        data = VK_UserActivity(domain=sys.argv[1], token=token).get_activity()
    except Exception as e:
        print(e)
        exit(1)

    with open(f'/home/leadness/{sys.argv[1]}.txt', 'w') as file:
        json.dump(data, file)