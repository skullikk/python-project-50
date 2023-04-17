#!/usr/bin/env python3
import json

import argparse


def bool_lower(dict_):
    for k in dict_.keys():
        if dict_.get(k) == True:
            dict_[k] = 'true'
        elif dict_.get(k) == False:
            dict_[k] = 'false'
    return dict_3


def generate_diff(file_path1, file_path2):
    dict_1 = bool_lower(json.load(open(file_path1)))
    dict_2 = bool_lower(json.load(open(file_path2)))
    dict_all = {**dict_1, **dict_2}
    sorted_dict_all = dict(sorted(dict_all.items()))
    str_result = ''
    for key in sorted_dict_all.keys():
        if dict_1.get(key) and dict_2.get(key) is None:
            str_result += f'  - {key}: {dict_1.get(key)}\n'
        elif dict_2.get(key) and dict_1.get(key) is None:
            str_result += f'  + {key}: {dict_2.get(key)}\n'
        elif dict_1.get(key) == dict_2.get(key):
            str_result += f'    {key}: {sorted_dict_all.get(key)}\n'
        elif dict_1.get(key) != dict_2.get(key):
            str_result += f'  - {key}: {dict_1.get(key)}\n  + {key}: {dict_2.get(key)}\n'
    return '{\n' + f'{str_result}' + '}'


def main():
    # print('Welcome!')
    parse = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parse.add_argument('first_file')
    parse.add_argument('second_file')
    parse.add_argument('-f', '--format', help='set format of output')
    args = parse.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
