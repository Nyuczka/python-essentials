def main():
    min_and_max()


def min_and_max():
    number = input('Enter a number: ')
    numbers = list()
    while number != "done":
        try:
            numbers.append(float(number))
        except:
            print('Invalid input')
        number = input('Enter a number: ')
    print('Maximum: {}'.format(max(numbers)))
    print('Minimum: {}'.format(min(numbers)))


main()
