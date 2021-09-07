hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        hoursAbove = hours - 40
        extraPayment = hoursAbove * 1.5 * rate
        result = (hours - hoursAbove) * rate + extraPayment
        print('Pay: {}'.format(result))
    else:
        print('Pay: {}'.format(hours * rate))
except:
    print('Error, please enter numeric input')

