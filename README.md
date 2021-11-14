# SL | String Search
The code searches for given substring in string in any order. 
Search string will search in the list of given strings in any order and return all those relevant strings.

## Features

- Search a string in any order
- Stop the search when it found the string present
- Accepts command line arguments for search
- Deals with only string types as of now

## Installation

This module is written in [python](https://www.python.org/) 3.8+.

This module does not require any additional dependencies. Just unzip the attachment and go to the dir and execute the below module with your existing virtualenv. 

### Clone the repository

```bash
git clone https://github.com/pritesh543/SL.git
cd SL
```

### OR | Download the Zip
Just extract the zip and go to the folder inside.

```bash
cd SL
```
Open your favorite Terminal and run these commands.

Main Code:

```python
python search.py -l "{list of words - comma separated}" -m "{seach string}"
# python search.py -l "seo,show,team,highlight,esopot" -m "eos"
# ["seo","esopot"]
```

Test Cases:

```python
pytest -v test_search.py
python test_search.py
```

## License
None
