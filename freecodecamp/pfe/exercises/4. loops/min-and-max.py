def min_and_max():
    number = input('Enter a number: ')
    result_min = None
    result_max = None
    while number != "done":
        try:
            number = float(number)
            if result_max is None and result_min is None:
                result_min = number
                result_max = number
            if result_min > number:
                result_min = number
            if result_max < number:
                result_max = number
        except:
            print('Invalid input')
        number = input('Enter a number: ')

    print('Results : min = {}, max = {}'.format(result_min, result_max))


min_and_max()
