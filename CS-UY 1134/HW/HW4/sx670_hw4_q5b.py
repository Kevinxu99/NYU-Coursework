def is_number_of_lowercase_even(s,low,high):
    if (low > high):
        return True
    rest_lc = is_number_of_lowercase_even(s, low + 1, high)
    if (ord(s[low]) >= ord('a') and ord(s[low]) <= ord('z')):
        if(rest_lc==True):
            return False
        else:
            return True
    else:
        return rest_lc