#!/usr/bin/env
# -*- coding: utf-8 -*-

import argparse
from io import StringIO
from random import SystemRandom

import pandas as pd
import requests

# Settings:
wordlist_url = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'
rolls = 5

#Cryptographically secure 👍👍
crypt_gen = SystemRandom()

def main(words):    
    #draw in the wordlist
    r = requests.get(wordlist_url)
    lst = r.text.replace('\t', ',')
    csv_list = StringIO(lst)

    # Process it a bit
    wordlist = pd.read_csv(csv_list, names=['key','word'])
    wordlist['key'] = wordlist['key'].astype(str)
    wordlist.set_index('key', inplace=True)

    return pass_gen(words, wordlist)


def roll(n):
    nums= [str(int(1 + crypt_gen.random()*6)) for i in range(n)]
    out = ''.join(nums)
    return out

def word(wordlist):
    return wordlist.loc[roll(rolls)].word

def pass_gen(w, wordlist):
    words = [word(wordlist) for i in range(w)]
    return ' '.join(words)


if __name__ == '__main__':
    cli_args = argparse.ArgumentParser(description='Generates a diceware password using the eff large wordlist')

    cli_args.add_argument(
        '-w', '--words',
        default=5,
        type=int,
        help='Set the number of words in the generated password(s).',
    )

    cli_args.add_argument(
        '-n', '--number',
        default=1,
        type=int,
        help='Set the number of passwords to generate. Useful when finding one you can more easily memorize.',
    )

    for i in range(cli_args.parse_args().number):
        print(main(cli_args.parse_args().words))

