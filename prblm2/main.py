def main(inp_str):
    '''
    inp_str: input data
    return: vowels used in the string
    '''

    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''

    for each_vow in vowels:
        if each_vow in inp_str:
            result = result + each_vow
    return result


if __name__ == '__main__':
    text1 = "Moon flowers bloom only at night, closing during the day,"
    text2 = "1 Yard (yd) = 3 feet (ft)."
    res1 = main(text1)
    print(res1)
    res2 = main(text2)
    print(res2)
