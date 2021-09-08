def main():
    print(color_value('X-DSPAM-Confidence: 0.8475 '))


def color_value(color_text):
    index_of_colon = color_text.find(':')
    color_text = color_text[index_of_colon + 1:len(color_text)]
    color_text = color_text.strip()
    return float(color_text)


main()
