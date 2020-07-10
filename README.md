# Phonetics Modeling (Python version)


This is the translation from the Haskell version.

## How to run
Run the following at the command line:

`python3 main.py`

So far it does most of what the Haskell version does, but cannot split IPA text into phonemes yet.

## How to run the tests:
Type the following line at the command line, and press enter.

`python3 -m unittest`


Plans:
- Create a program that processes phonetics data,  and represents concepts from phonology.
- Use the Python programming language.
- Make it follow closely the design decisions in the phonetics-modeling project at http://github.com/elsanussi-s-mneina/phonetics-modeling

## Current Issues
- splitting IPA text into phonemes does not work
- more unit tests wanted
- neeed to rename identifiers to be consistent (specifically using snake-case, and consistent use or lack of use of abbreviations)