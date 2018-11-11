import vk_api
import get_friend_list
import check_name_in_file


def write_info(first_name, oficial_name, us_id, con, username, passwordik):
    friends_list = get_friend_list.get_friends(us_id, username, passwordik)

    if friends_list == [1]:
        return 0

    friends_list = friends_list["items"]

    if len(friends_list) == 0:
        return 0

    print(len(friends_list), con)

    if con < 2:
        for i in range(len(friends_list)):
            if con == 0:
                print("HERE", i)
            print(i)
            if friends_list[i]["first_name"] == first_name or friends_list[i]["first_name"] == oficial_name:
                friend_info = friends_list[i]["first_name"] + " " + friends_list[i]["last_name"]
                friend_info += " " + str(friends_list[i]["id"])
                if check_name_in_file.check_name(friend_info) == 0:
                    f = open("us_id", 'ta', encoding='utf-8')
                    print(friend_info, file=f)
                    f.close()

            print(friends_list[i]["first_name"])
            write_info(first_name, oficial_name, str(friends_list[i]['id']), con+1, username, passwordik)

    elif con == 2:
        print(friends_list)
        for i in range(len(friends_list)):
            if friends_list[i]["first_name"] == first_name or friends_list[i]["first_name"] == oficial_name:
                friend_info = friends_list[i]["first_name"] + " " + friends_list[i]["last_name"]
                friend_info += " " + str(friends_list[i]["id"])
                if check_name_in_file.check_name(friend_info) == 0:
                    f = open("us_id", 'ta', encoding='utf-8')
                    print(friend_info, file=f)
                    f.close()