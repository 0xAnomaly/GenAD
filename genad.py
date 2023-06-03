#!/usr/bin/env python3

import sys

def generate_username(name, surname):
    first = name[0].lower()
    last = surname[0].lower()

    username_options = [
        name, 
        surname,
        first + '.' + surname,
        first + surname,
        name + last,
        name + '.' + last,
        name + '.' + surname,
        name + '_' + surname,
        first + '_' + surname,
        name + '_' + last,
        first + '-' + surname,  
        name + '-' + last,
        last + '-' + name,
        name + surname,
        surname + name
    ]

    return username_options

if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

infile = sys.argv[1]

with open(infile, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    temp = line.split()
    name = temp[0].lower()
    surname = ' '.join(temp[1:]).lower()

    usernames = generate_username(name, surname)

    for username in usernames:
        print(username)

file.close()
