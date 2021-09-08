
def main():
    filename = input('Enter the file name: ')
    print('Average spam confidence: {}'.format(spam_lines_count(filename)))


def spam_lines_count(filename):
    sum_of_confidence = 0
    count = 0
    try:
        file = open(filename)
        for line in file:
            if 'X-DSPAM-Confidence' in line:
                sum_of_confidence += color_value(line)
                count += 1
    except:
        print('Bad file name')
        quit()
    if count != 0:
        return sum_of_confidence/count
    return 0


def color_value(color_text):
    index_of_colon = color_text.find(':')
    color_text = color_text[index_of_colon + 1:len(color_text)]
    color_text = color_text.strip()
    return float(color_text)


main()
