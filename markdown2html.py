#!/usr/bin/python3
"""Markdown"""

import os
import sys


def counter(str):
    """count the chars"""
    count = 0
    for i in str:
        if i == "#":
            count = count + 1
        if i == ' ':
            break
    return count

if __name__ == "__main__":
    """markdown"""
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as f:
        html_lines = []
        flag = 0
        for line in f.readlines():
            if line[0] == '#':
                count = counter(line)
                html_lines.append('<h{0}>{1}</h{0}>\n'.format(str(count), line[count+1:-1]))

            if line[0] == '-':
                if flag != 1:
                    html_lines.append('<ul>\n')
                    flag = 1
                html_lines.append('<li>{}</li>\n'.format(line[2:-1]))
            if flag == 1 and line[0] != '-':
                html_lines.append('</ul>\n')
                flag = 0

            if line[0] == '*':
                if flag != 2:
                    html_lines.append('<ol>\n')
                    flag = 2
                html_lines.append('<li>{}</li>\n'.format(line[2:-1]))
            if flag == 2 and line[0] != '*':
                html_lines.append('</ol>\n')
                flag = 0

        if flag == 1:
            html_lines.append('</ul>\n')
        if flag == 2:
            html_lines.append('</ol>\n')


    with open(sys.argv[2], 'a') as htm:
        for h_line in html_lines:
            htm.write(h_line)


    exit(0)
