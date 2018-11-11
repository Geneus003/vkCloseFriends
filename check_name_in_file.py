def check_name(name):
    f = open("us_id", "r")
    strocchka = ""
    for line in f:
        strocchka += line

    if strocchka.find(name) == -1:
        return 0
    else:
        return 1


check_name("Татьян Арсеньева 22929")