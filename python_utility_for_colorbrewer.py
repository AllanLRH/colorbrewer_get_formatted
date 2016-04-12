#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
import re
import sys
import argparse
import pyperclip

parser = argparse.ArgumentParser('colorbrewer_colors')
parser.add_argument('url', help='Permalink to colormap', type=str)
parser.add_argument('-n', '--normalized', help="Output formattet as rgb (values in range 0-1) instead of RGB (range 0-255)", action='store_true', default=False)
parser.add_argument('-c', '--copy', help="Put the color matrix in the clipboard", action='store_true', default=False)
parser.add_argument('-p', '--print', help="Don't print the color matrix', action='store_false", default=True)
args = parser.parse_args()

m = re.match(r'http://colorbrewer2.org/.+scheme=(.+?)&n=(\d+)', args.url)
if not m:
    print("Error! Check input url!", file=sys.stderr)
    sys.exit(1)
gimplink = 'http://colorbrewer2.org/export/gpl/{}_{}.gpl'.format(*m.groups())

r = requests.get(gimplink)
if r.status_code != 200:
    print("Error, retrieving colorbrewer data!", file=sys.stderr)
    sys.exit(1)

res = re.findall(r'(\d{1,3} {1,3})', r.text, re.MULTILINE)
RGB = list()
rgb = list()
for i in range(0, len(res), 3):
    innerRGB = list()
    innerrgb = list()
    for j in range(3):
        n = res[i+j]
        innerRGB.append('{:03d}'.format(int(n)))
        innerrgb.append('{:.3f}'.format(int(n)/255))
    endChar = ';' if len(rgb) != len(res)/3-1 else '];'
    beginChar = ' ' if len(rgb) else ''
    RGB.append(beginChar + ' '.join(innerRGB[:]) + endChar)
    rgb.append(beginChar + ' '.join(innerrgb[:]) + endChar)

colorMatrix = '[' + '\n'.join(rgb) if args.normalized else '[' + '\n'.join(RGB)

if args.copy:
    pyperclip.copy(colorMatrix)

if args.print:
    print(colorMatrix)
