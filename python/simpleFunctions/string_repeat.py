def repeatStr(string, repeat = 2, seperator = ""):

    """repeatStr function used for repeat a string with number of repeat and 
    seprator between strings"""
    final_string = string
    while repeat > 1:
        final_string +=  seperator + string
        repeat -= 1

    return final_string


