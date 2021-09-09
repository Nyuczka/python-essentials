
def main():
    read_upper_cased('mbox-short.txt')


def read_upper_cased(filename):
    try:
        file = open(filename)
        print('Enter a file name: {}'.format(file.name))
        for line in file:
            if line.startswith('X-Sieve'):
                break
            print(line.upper().rstrip())
    except:
        print('Error while opening a file')
        quit()


main()
