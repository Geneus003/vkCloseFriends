import vk_api


def get_friends(target_id, username, passwordik):
    login, password = username, passwordik

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    friend_list = vk.friends.get(user_id=target_id, fields="nickname")

    return friend_list

