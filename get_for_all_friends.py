import vk_api
import get_friend_list


def write_info(first_name, us_id, con, username, passwordik):
    friends_list = get_friend_list.get_friends(us_id, username, passwordik)

    if friends_list == [1]:
        return

    friends_list = friends_list["items"]

    print(friends_list)

    if con != 1:
        f = open("us_id", 'tw', encoding='utf-8')
        for i in range(len(friends_list)):
            if friends_list[i]["first_name"] == first_name:
                print(friends_list[i]["first_name"], friends_list[i]["last_name"], friends_list[i]["id"], file=f)

            write_info(first_name, friends_list[i]['id'], con+1, username, passwordik)

        f.close()
    else:
        f = open("us_id", 'tw', encoding='utf-8')
        for i in range(len(friends_list)):
            if friends_list[i]["first_name"] == first_name:
                print(friends_list[i]["first_name"], friends_list[i]["last_name"], friends_list[i]["id"], file=f)

            write_info(first_name, friends_list[i]['id'], con, username, passwordik)