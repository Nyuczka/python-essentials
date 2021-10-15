import os


def main():
    returned_list = emails('../../resources/mbox-short.txt')
    print_emails(returned_list)


def print_emails(returned_list):
    if len(returned_list) == 0:
        print('No elements in list.')
    else:
        for email in returned_list:
            print(email)
    print('There were {} lines in the file with From as the first word'.format(len(returned_list)))


def emails(filename):
    emails_list = list()
    try:
        file = open(filename)
        for line in file:
            line = line.lstrip()
            if line.startswith('From'):
                email_split = line.split()
                if email_split[1] not in emails_list:
                    emails_list.append(email_split[1])
        return emails_list
    except:
        print('Error while reading file: %s' % filename)
        quit()


main()
