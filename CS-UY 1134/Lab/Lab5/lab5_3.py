def is_palindrome(input_str,low,high):
    if(low>=high):
        return True
    if(is_palindrome(input_str,low+1,high-1)):
        if(input_str[low]==input_str[high]):
            return True
        else:
            return False
    else:
        return False