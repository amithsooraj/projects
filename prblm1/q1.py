from datetime import datetime as dt


def parse_file(fname):
    '''
    fname: path to the input file
    returns: dictionary containing name, age pairs
    '''
    cntr = 1
    names, ages = [], []
    with open(fname, 'r') as fl:
        for line in fl:
            line = line.strip()
            if cntr % 2 != 0:
                names.append(line)
            else:
                ages.append(line)
            # increment line counter
            cntr += 1
    data = dict(zip(names, ages))
    return data


def sort_dict(data):
    '''
    dict: Dictionary containing name, age
    return sorted dictionary
    '''
    sorted_data = dict(
        sorted(data.items(),
               key=lambda item: dt.strptime(item[1], '%d-%m-%Y'),
               reverse=True),
    )
    return sorted_data


if __name__ == '__main__':
    data = parse_file('ag1.txt')
    sorted_data = sort_dict(data)
    names = list(sorted_data.keys())
    youngest = names[0]
    print(youngest)
