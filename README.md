# My solutions for Advent of Code 2024

## Setup

After cloning this repository, create a virtual environment, activate it, and install.

```bash
$ cd python-aoc2024
python-aoc2024$ python -m venv venv
python-aoc2024$ . venv/bin/activate
(venv) python-aoc2024$ pip install -e .[test]
```

## Create new daily workspace

```bash
(venv) python-aoc2024$ newday 1
```

## Run daily solutions

```bash
(venv) python-aoc2024$ python aoc2024/day01/solution.py 
69626
206780
```

## Test Suite
Run tests fro individual days with `pytest tests/test_day##.py`

```bash
(venv) python-aoc2024$ pytest --cov
======================================================================== test session starts =========================================================================
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/vance/git/github.com/vmorris/python-aoc2024
plugins: cov-6.0.0
collected 6 items                                                                                                                                                    

tests/test_day01.py ..                                                                                                                                         [ 33%]
tests/test_day02.py ..                                                                                                                                         [ 66%]
tests/test_day03.py ..                                                                                                                                         [100%]

---------- coverage: platform linux, python 3.12.7-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
aoc2024/__init__.py             0      0   100%
aoc2024/day01/solution.py      23      0   100%
aoc2024/day02/solution.py      35      0   100%
aoc2024/day03/solution.py       5      0   100%
aoc2024/util.py                37     19    49%
tests/test_day01.py            11      0   100%
tests/test_day02.py            11      0   100%
tests/test_day03.py            11      0   100%
-----------------------------------------------
TOTAL                         133     19    86%
```
