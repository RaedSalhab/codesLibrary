from string_length import string_length

def string_left_trim(a_string, trimed):
    """Function for delete trimed character from starting of a_string
    1- create index variable equal 0
    2- create while loop when index less than a_string length
    3- use if statement with condition a_string[index] != trimed
    4- when condition is true break while loop 
    5- when condition id false index increses by 1
    6- return slice a_string starting from index to end 
    """
    index = 0
    while index < string_length(a_string):
        if a_string[index] != trimed:
            break
        index += 1
    
    return a_string[index:]