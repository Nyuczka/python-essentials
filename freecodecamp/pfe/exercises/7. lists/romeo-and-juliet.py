def main():
    print(romeo_and_juliet('../../resources/romeo.txt'))


def romeo_and_juliet(filename):
    result_list = list()
    try:
        file = open(filename)
        for line in file:
            split_list = line.split()
            for split in split_list:
                if split not in result_list:
                    result_list.append(split)
    except:
        print('Could not process the file: {}'.format(filename))
        quit()
    result_list.sort()
    return result_list


main()
