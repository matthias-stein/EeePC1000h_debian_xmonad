#!/usr/bin/env python3
import re

from pathlib import Path
from textwrap import wrap, indent

path = Path('/home/matthias/.xmonad/xmonad.hs')
# re01 = re.compile('(\("M-)(.+)(--)')  # identifies line with shortcut definition
re01 = re.compile(r'\("M-')  # identifies line with shortcut definition
re02 = re.compile(r'"\s*,\s')  # splits shortcut from command/comment
re03 = re.compile(r'\)\s+--\s')  # splits comment from command
re04 = re.compile(r'(,\s+)?\("')  # tidies up shortcut
prev = None  # saves previous line's content in case of \-continuatiom
klen = 0  # max shortcut key combination lenght
kmap = {}  # keymap with explanations extracted from xmonad.hs

with open(path, 'r') as hndl:
    for line in hndl.readlines():
        line = line.strip()

        if line[:2] != '--':
            # remove commented out lines

            if line[:1] == "\\" and prev is not None:
                # previous line ended with continuation backslash,
                # current line starts with continuation backslash,
                # pre-pend previous line to current
                line = prev + line[1:]
                prev = None

            if line[-1:] == "\\":
                prev = line[:-1]
            elif re01.search(line):
                tmp1 = re02.split(line)
                keyc = re04.sub('', tmp1[0])
                tmp2 = re03.split(tmp1[1])

                try:
                    expl = tmp2[1]
                except IndexError:
                    # no comment at end of line, display command
                    expl = tmp2[0]

                if keyc.__len__() > klen:
                    klen = keyc.__len__()
                kmap[keyc] = expl

titl = 'XMONAD Shortcuts'
tsep = titl.__len__() * '='
print()
print(titl)
print(tsep)
print()

for skey, expl in kmap.items():
    dlim = ' - '
    skey = skey.ljust(klen, ' ')
    expl = wrap(expl, 79 - dlim.__len__() - klen)

    print(skey, dlim, expl[0], sep='')
    for item in expl[1:]:
        pfix = (klen + dlim.__len__()) * ' '
        print(indent(item, pfix))

print()
while True:
    inpt = input("Press q to quit: ")
    if inpt == 'q':
        exit()
