#!/usr/bin/env python3 

import argparse
import json

from pathlib import Path

deck = (
    (
        ('xmobar/home/matthias/.config/xmobar/'),
        ('_xmobarrc_theme_template'),
        ('xmobarrc')
    ),
    (
        ('xmonad/home/matthias/.xmonad'),
        ('_xmonad.hs_theme_template'),
        ('xmonad.hs')
    ),
    (
        ('stalonetray/home/matthias'),
        ('_stalonetrayrc_theme_template'),
        ('.stalonetrayrc')
    ),
    (
        ('xsessionrc/home/matthias'),
        ('_xsessionrc_theme_template'),
        ('.xsessionrc')
    )
)

prsr = argparse.ArgumentParser(
    description='Deploy a theme',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter 
)
prsr.add_argument(
        '-n',
        '--name',
        choices=['dracula', 'nord', 'solarized'],
        required=True,
        help='name of theme to deploy'
)
args = prsr.parse_args()

path_list = Path(__file__).resolve().parents
path_base = path_list[1]
path_them = path_list[0]

json_path = path_them / 'theme-{name}.json'.format(name=args.name)
print('\n[READING THEME FILE]\n   ', json_path)
with open(json_path, 'r') as json_hndl:
    json_data = json.load(json_hndl)

for item in deck:
    srce = path_base / item[0] / item[1]
    dest = path_base / item[0] / item[2]
    print('\n[PROCESSING\n   ', srce, '\n    =>\n   ', dest)

    with open(srce, 'r') as hndl:
        rslt = hndl.read()
    
    rslt = rslt.replace('{{ logo }}', json_data['logo'])
    rslt = rslt.replace('{{ wall }}', json_data['wall'])
    rslt = rslt.replace('{{ xdmb }}', json_data['xdmb'])
    rslt = rslt.replace('{{ back }}', json_data['back'])
    rslt = rslt.replace('{{ forg }}', json_data['forg'])
    rslt = rslt.replace('{{ easy }}', json_data['easy'])
    rslt = rslt.replace('{{ norm }}', json_data['norm'])
    rslt = rslt.replace('{{ high }}', json_data['high'])
    rslt = rslt.replace('{{ prog }}', json_data['prog'])
    rslt = rslt.replace('{{ wsab }}', json_data['wsab'])
    rslt = rslt.replace('{{ wsaf }}', json_data['wsaf'])
    rslt = rslt.replace('{{ wsib }}', json_data['wsib'])
    rslt = rslt.replace('{{ wsif }}', json_data['wsif'])
    rslt = rslt.replace('{{ bocn }}', json_data['bocn'])
    rslt = rslt.replace('{{ bocf }}', json_data['bocf'])
    rslt = rslt.replace('{{ test }}', 'test')

    with open(dest, 'w') as hndl:
        hndl.write(rslt)

