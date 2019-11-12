from VK_UserActivity import *

if __name__ == '__main__':
    with open('config/default_config.json', 'r') as file:
        token = json.load(file)['vk_token']

    domain = input("Enter domain: ")
    try:
        user = VK_UserActivity(domain=domain, token=token)
        print('Start monitoring %s[%s]' % ((user.get_first_name() + ' ' + user.get_last_name()), domain))
    except Exception as e:
        print(e)
        exit(1)
    while True:
        user.check_user_activity()
        sleep(60)
