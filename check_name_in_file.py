def check_name(name):

    # Function to check user in list
    # Do not change the file name or attributes
    
    f = open("us_id", "r")
    all_users_in_str = ""
    for line in f:
        all_users_in_str += line

    if all_users_in_str.find(name) == -1:
        return 0
    else:
        return 1


check_name("Татьян Арсеньева 22929")