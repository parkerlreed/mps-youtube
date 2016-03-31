""" Module for holding colour code values. """

import os
import re
import sys

try:
    # pylint: disable=F0401
    from colorama import Fore, Style
    has_colorama = True

except ImportError:
    has_colorama = False

    ul = red = green = yellow = blue = pink = white = ""

r, g, y, b, p, w = red, green, yellow, blue, pink, white

ansirx = re.compile(r'\x1b\[\d*m', re.UNICODE)

def c(colour, text):
    """ Return coloured text. """
    colours = {'r': r, 'g': g, 'y': y, 'b':b, 'p':p}
    return colours[colour] + text + w

def charcount(s):
    """ Return number of characters in string, with ANSI color codes excluded. """
    return len(ansirx.sub('', s))
