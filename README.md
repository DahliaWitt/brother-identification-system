# Brother Identification System

Facial recognition software to identify brothers entering our chapter haus. 

## Requirements

- Python 3.7
- Anaconda or Miniconda
- dlib [Installation instructions here](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

## Getting the environment set up

- Create the environment from the file `conda env create -f environment.yml`
- Activate the environment (conda should give you the command upon creating the environment)
- Add your brothers module (directions below)

## Brothers Module

For privacy, there is an additional module that is git-ignored. The module contains the images, image paths, and names of every known face. Make the directory of this form:
- `__init__.py` - this should contin two arrays, BROTHERS (image url) and BROTHERS_NAMES (name in string)
- `images` - directory with all the face images

## Running

`python main.py`

## Issues

Facial recognition is really slow, looking at ways to optimize

