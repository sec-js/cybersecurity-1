#!/usr/bin/env python3


__author__ = "Alexis Rodriguez"
__date__   = 12_12_2020


from colored import fg, attr
from sys import stdin, exit
from os.path import exists, isdir, isfile
from utils.prog_args import arg_parse
from random import randint

# encoding
from src.encoding import url
from src.encoding import hex
from src.encoding import bases
from src.encoding import binary

# hashing

# encryption

# compression

color = lambda s: ("%s" + s + "%s") % (fg(randint(1, 220)), attr(0))


def main():
    args = arg_parse()  

    try:
        lines = stdin.readlines()
    # capture CTRl + d
    except EOFError:
        pass

    if lines[-1][-1] == '\n':
        pass
    else:
        print()

    std_in = "".join([ line.strip() for line in lines ])

    # BASE Encoding -------------------
    if args.base85:
        print(color("Base85:"), bases.eighty_five(std_in))
    if args.from_base85:
        print(color("Decoded Base85:"), bases.eighty_five_decode(std_in))
    if args.base64:
        print(color("Base64:"), bases.sixty_four(std_in))
    if args.from_base64:
        print(color("Decoded Base64:"), bases.sixty_four_decode(std_in))
    if args.base32:
        print(color("Base32:"), bases.thirty_two(std_in))
    if args.from_base32:
        print(color("Decoded Base32:"), bases.thirty_two_decode(std_in))
    if args.base16:
        print(color("Base16:"), bases.sixteen(std_in))
    if args.from_base16:
        print(color("Decoded Base16:"), bases.sixteen_decode(std_in))

    # HEX Encoding --------------------
    if args.hexadecimal:
        print(color("Hex:"), hex.hx(std_in))
    if args.from_hexadecimal:
        print(color("Decode Hex:"), hex.hx(std_in))
    if args.hexdump:
        print()
        hex.hxd(std_in)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n' + color("Goodbye..."))