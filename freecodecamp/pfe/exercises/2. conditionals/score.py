
score = input("Enter your score: ")

try:
    score = float(score)
    if 0.9 <= score <= 1:
        print('A')
    elif 0.8 <= score < 0.9:
        print('B')
    elif 0.7 <= score < 0.8:
        print('C')
    elif 0.6 <= score < 0.7:
        print('D')
    elif 0 <= score < 0.6:
        print('F')
    else:
        print('Bad score')
except:
    print('Please enter numeric input')