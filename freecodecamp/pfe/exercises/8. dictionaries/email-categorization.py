def main():
    result = process_file('../../resources/mbox.txt')
    print(result)


def process_file(filename) -> dict:
    result = {}
    try:
        file = open(filename)
        for line in file:
            if line.startswith("From"):
                categorize_email(line, result)
        return result
    except FileNotFoundError:
        print("The file doesn't exists")
        quit()


def categorize_email(text_line: str, result: dict):
    day_of_week = text_line.strip().split(' ')
    if len(day_of_week) > 2:
        day_of_week = day_of_week[2]
        if day_of_week not in result:
            result[day_of_week] = 0
        else:
            result[day_of_week] += 1


main()
