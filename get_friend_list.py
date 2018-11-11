import vk_api


def get_friends(target_id, username, passwordik):

    # This functions gets list of friends for actual user
    # Do not fix here anything and you shouldn't forget about counter of requests(more than 3000)

    login, password = username, passwordik

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    try:
        friend_list = vk.friends.get(user_id=target_id, fields="nickname")
    except vk_api.exceptions.ApiError as error_msg:
        return [1]
    return friend_list

