import argparse


def main():
    # print('Welcome!')
    parse = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parse.add_argument('first_file')
    parse.add_argument('second_file')
    parse.add_argument('-f', '--format', help='set format of output')
    args = parse.parse_args()



if __name__ == '__main__':
    main()
