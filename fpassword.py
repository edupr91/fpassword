#!/usr/bin/python3

from pykeepass import PyKeePass
from PyInquirer import prompt
import pyperclip
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(
    description='Find & copy passwords to your clipboard from a KDBX file'
)
parser.add_argument('string',
                    help='String to find')
args = vars(parser.parse_args())
to_find = args['string']

# KDBX files
db_kdbx = '/path/to/you/file.kdbx'
db_key = '/path/to/you/file.kdbx'
db_password = 'MySuperSecurePassword'
kp = PyKeePass(db_kdbx, keyfile=db_key, password=db_password)

entries_found = kp.find_entries(
    title='(?i).*{}.*'.format(to_find), regex=True, first=False
)
entries_found_dic = {}
counter = 0
for entry in entries_found:
    entry_name = str(entries_found[counter]).\
        replace('Entry: "', '').\
        replace('"', '')
    entries_found_dic[entry_name] = entries_found[counter]
    counter += 1

entries_list_keys = list(entries_found_dic.keys())

questions = [
    {
        'type': 'list',
        'name': 'Entry',
        'message': 'This is what I found',
        'choices': entries_list_keys,
    },
]

answer = prompt(questions)
title = str(answer).replace("{'Entry': '", '').replace("'}", '')
pyperclip.copy(entries_found_dic[title].password)
print('URL: {}'.format(entries_found_dic[title].url))
colored_passwd = colored(
    entries_found_dic[title].password,
    'white',
    'on_white')
print('username: {}'.format(entries_found_dic[title].username))
print('Password: {}'.format(colored_passwd))
print('Password copied to clipboard')
