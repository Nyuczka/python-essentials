def main():
    file_name = 'mbox-short.txt'
    email_count = get_email_count_from_file(file_name)
    count_with_tuple(email_count)


def get_email_count_from_file(file_name) -> dict:
    result = {}
    try:
        file = open('../../resources/' + file_name)
        for line in file:
            count_email(line, result)
        return result
    except FileExistsError:
        print('File does not exist.')
        quit(500)


def count_email(line: str, result: dict):
    count = 1
    if line.startswith('From'):
        email = line.strip().split(' ')[1]
        if email not in result:
            result[email] = count
        else:
            result[email] += 1


def count_with_tuple(dictionary: dict):
    dictionary_tuple = list((v, k) for k, v in dictionary.items())
    sorted_tuple = sorted(dictionary_tuple, reverse=True)
    email, count = sorted_tuple[0]
    print(count + " " + str(email))


main()
