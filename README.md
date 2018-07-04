## Password Generator

Very simple diceware password generator. Uses SystemRandom for a cryptographically strong random generation... though it's more for novelty, as for my purposes it's definitely overkill.

## Requirements

* python 3
* pandas
* requests

## Usage

Pretty simple:
```
python pass_gen.py
```

Generates a diceware password of 5 words. Uses the EFF's large wordlist, though the code can easily be altered.

options:
* -w, --words
    * Number of words per password
* -n, --number
    * Number of passwords to generate


