def validate_pwd(pwd):
    '''
    pwd: Password to be validated
    return: True if pwd is valid, else returns False
    '''

    if not (len(pwd) >= 8 and len(pwd) <= 32):
        return False
    elif not (str.isalpha(pwd[0])):
        return False

    invalid_chars = ['/', "\\", '=', "'", '"', ' ']
    for each_char in pwd:
        if each_char in invalid_chars:
            return False
            break

    return True


if __name__ == '__main__':
    res1 = validate_pwd('abcd')
    res2 = validate_pwd('a'*33)
    res3 = validate_pwd('1abcdefge')
    res4 = validate_pwd('a/')
    res5 = validate_pwd('abcdefgh')
    res6 = validate_pwd('a\\bcdefgh')
    print(res1, res2, res3, res4, res5, res6)
