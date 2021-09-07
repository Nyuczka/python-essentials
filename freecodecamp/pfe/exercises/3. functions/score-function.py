def main():
    try:
        score = input('Enter score: ')
        score = float(score)
        compute_grade(score)
    except ValueError:
        print('Error, please enter numeric input')


def compute_grade(score: float):
    if 0.9 <= score <= 1:
        print('A')
    elif 0.8 <= score < 0.9:
        print('B')
    elif 0.7 <= score < 0.8:
        print('C')
    elif 0.6 <= score < 0.7:
        print('D')
    else:
        print('Bad score')


main()
