# My Advent of Code solutions
[Advent of Code](https://adventofcode.com) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. I mainly use Python and sometimes also R or Java.

| Year | Stars |
|------|------:|
| 2018 |   8 ⭐ |
| 2019 |  44 ⭐ |
| 2020 |  50 ⭐ |
| 2021 |  50 ⭐ |
| 2022 |   4 ⭐ |

## Preparing for a day
Run `prepare.py` to download the input and generate the script and tests from templates for the current day.
The optional arguments are `year` and `day` with the current year and day as default values.
Run `prepare.py --all-inputs` to download the inputs of all challenges so far.

To be able to download the input data you need to have your session cookie stored in a file with the name `secrets.json` in the root of this repository.
The file must contain the value of the cookie as a string with the key "session_cookie".
You can get your current cookie from the website while being logged in.
Remember that it expires after one month.

## Running the scripts
Run `aoc.py` to run the script for the current day. Use the arguments `year` and `day` to specify a different date.  
Example: `python aoc.py 2021 10` runs Advent of Code 2021-12-10.

## Testing
Run `test.py` to run all tests in the `test` directory.
Use the optional arguments `year` and `day` to run only one year or only one day from that year.
With `--skip-samples` the scripts are only checked against the real inputs.
With `--verbosity` followed by an integer you can control the amount of `unittest` output.
0 is quiet, 1 is just the dots (default), and 2 is verbose.

Remember that most participants get different input data so the results in the comments and unit tests will likely be different from yours.

**Please note that the above information about running and testing the solutions does not apply to 2019.
I still need to rewrite the scripts of that year.**
