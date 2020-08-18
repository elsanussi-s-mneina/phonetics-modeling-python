# Phonetics Modeling (Python version)

To see a demonstration of the program, without having to install it, please [see the screenshots](https://github.com/elsanussi-s-mneina/phonetics-modeling-python/wiki/screenshots).

# Requirements
- Python 3.8

## How to run
Run the following at the command line:

`python3 main.py`


## How to run the tests:
Type the following line at the command line, and press enter.

`python3 -m unittest`


Plans:
- Create a program that processes phonetics data,  and represents concepts from phonology.
- Use the Python programming language.
- Make it follow closely the design decisions in the phonetics-modeling project at http://github.com/elsanussi-s-mneina/phonetics-modeling

This is the translation from the Haskell version.

## How to use Docker

Build the image by running the following command:

`docker build -t phonetics-modeling-python .`

Start the Docker container. This will start the server.
`docker run -p 8770:8080 phonetics-modeling-python`

Now open your browser, and browse to:
  `http://localhost:8770/voice_phoneme/s`

OR:
 `http://localhost:8770/voice_phoneme/s`

## Current Issues
- more unit test coverage to be added
