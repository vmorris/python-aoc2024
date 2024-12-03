# My solutions for Advent of Code 2024

## Setup

After cloning this repository, create a virtual environment, activate it, and install.

```
$ cd aoc2023
aoc2022 $ python3 -m venv venv
aoc2022 $ . venv/bin/activate
(venv) aoc2022 $ pip install -e .[test]
```

## Create new daily workspace

```
(venv) aoc2022 $ newday 1
```

## Run daily solutions

```
(venv) [vmorris@tpp53 aoc2022]$ python aoc2022/day01/solution.py 
69626
206780
```

## Test Suite
Run individual days with `pytest tests/test_day##.py`

```
(venv) [vmorris@tpp53 aoc2022]$ pytest --cov=aoc2022
=============================== test session starts ===============================
platform linux -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/vmorris/git/github.com/vmorris/aoc2022
plugins: cov-4.0.0
collected 14 items                                                                

tests/test_day01.py ..                                                      [ 14%]
tests/test_day02.py ..                                                      [ 28%]
tests/test_day03.py ..                                                      [ 42%]
tests/test_day04.py ..                                                      [ 57%]
tests/test_day05.py ..                                                      [ 71%]
tests/test_day06.py ..                                                      [ 85%]
tests/test_day07.py ..                                                      [100%]

---------- coverage: platform linux, python 3.11.0-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
aoc2022/day01/solution.py      24      0   100%
aoc2022/day02/solution.py      75     24    68%
aoc2022/day03/solution.py      23      0   100%
aoc2022/day04/solution.py      20      0   100%
aoc2022/day05/solution.py      47      0   100%
aoc2022/day06/solution.py      14      0   100%
aoc2022/day07/solution.py      50      1    98%
aoc2022/util.py                26     10    62%
-----------------------------------------------
TOTAL                         279     35    87%


=============================== 14 passed in 0.11s ================================
```
