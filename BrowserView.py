from selenium import webdriver
import random, time


def open_in_browser(road):
    driver = webdriver.Chrome()
    driver.get("https://www.vk.com/id" + road)

    temp_time = random.randint(25, 35)

    print("You have", temp_time, "seconds")

    time.sleep(temp_time)

    driver.close()


working_file = open("us_id", "r")

all_users_in_str = ""
for line in working_file:
    all_users_in_str += line

mas_friends = []

cor = 0
get_id = ""
for i in range(len(all_users_in_str)):
    if all_users_in_str[i].isdigit() == 1 and cor == 0:
        cor = 1
        get_id += all_users_in_str[i]

    elif cor == 1 and all_users_in_str[i] != " ":
        get_id += all_users_in_str[i]

    if all_users_in_str[i].isdigit() == 0 and cor == 1:
        print(get_id)
        open_in_browser(get_id)
        get_id = ""
        cor = 0
