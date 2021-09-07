def main():
    hours = input('Enter hours: ')
    rate = input('Enter rate: ')

    try:
        hours = float(hours)
        rate = float(rate)
        compute_pay(hours, rate)
    except TypeError:
        print('Error, please enter numeric input')


def compute_pay(hours: float, rate: float):
    if hours > 40:
        above = hours - 40
        print('Pay: {}'.format((hours - above) * rate + 1.5 * above * rate))
    else:
        print('Pay: {}'.format(hours * rate))


main()
