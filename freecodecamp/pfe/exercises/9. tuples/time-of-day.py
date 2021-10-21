def main():
    file_name = 'mbox-short.txt'
    result = get_hours_count(file_name)
    print_hours(result)


def get_hours_count(file_name) -> dict:
    result = {}
    try:
        file = open('../../resources/' + file_name)
        for line in file:
            count_hours(line, result)
        return result
    except FileExistsError:
        print('File does not exist.')
        quit(500)


def count_hours(line: str, result: dict):
    count = 1
    if line.startswith('From'):
        split = line.strip().split(' ')
        for element in split:
            if ":" in element and "From" not in element:
                hour = element.split(':')[0]
                result[hour] = count if hour not in result else count + 1


def print_hours(dictionary: dict):
    toppled = sorted((k, v) for k, v in dictionary.items())
    for hour, count in toppled:
        print("{} {}".format(hour, count))


main()
