def main():
    filename = input('Enter filename: ')
    result = process_file('../../resources/' + filename)
    print(result)
    print(get_most_emailed_name(result))


def process_file(filename) -> dict:
    result = {}
    try:
        file = open(filename)
        for line in file:
            if line.startswith('From'):
                count_emails(line, result)
        return result
    except FileExistsError:
        print('File does not exist')
        quit(500)


def count_emails(text_line: str, dictionary: dict):
    email = text_line.strip().split(' ')[1]
    if email not in dictionary:
        dictionary[email] = 0
    else:
        dictionary[email] += 1


def get_most_emailed_name(dictionary: dict):
    return max(dictionary, key=dictionary.get)


main()
