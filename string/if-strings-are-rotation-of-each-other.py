

def is_rotated(str_1, str_2):

    if len(str_1) != len(str_2):
        return False

    str_1 += str_1

    if str_2 in str_1:
        return True
    return False


print(is_rotated( "aacd", "acd" ))