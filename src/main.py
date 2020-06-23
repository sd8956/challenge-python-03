import re


def run():
    with open('encoded.txt','r', encoding='utf-8') as file:
        regex = re.compile('[a-z]')
        message = re.findall(regex, file.read())
        print(''.join(message))


if __name__ == '__main__':
    run()
