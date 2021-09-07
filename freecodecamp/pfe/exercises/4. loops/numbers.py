def number_count():
    entries_count = 0
    numbers_sum = 0
    number = input('Enter a number: ')
    while number != "done":
        try:
            number = float(number)
            entries_count = entries_count + 1
            numbers_sum = number + numbers_sum
        except:
            print('Invalid input')
        number = input('Enter a number: ')
    print('Results: {} {} {}'.format(int(numbers_sum), entries_count, numbers_sum / entries_count))


number_count()
