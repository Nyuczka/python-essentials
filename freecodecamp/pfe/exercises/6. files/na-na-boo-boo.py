def main():
    filename = input('Enter the file name: ')
    print(subject_lines_count(filename))


def subject_lines_count(filename):
    count = 0
    if filename == 'na na boo boo':
        return 'NA NA BOO BOO TO YOU - You have been punk\'d!'
    try:
        file = open(filename)
        for line in file:
            if line.startswith('Subject'):
                count += 1
        return 'There were {} subject lines in {}'.format(count, filename)
    except:
        print('File cannot be opened: {}'.format(filename))
        quit()


main()
