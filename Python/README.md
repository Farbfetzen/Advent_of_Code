# Python solutions for Advent of Code

Please note that the information about running and testing the solutions does not apply to 2019.
I still need to rewrite many of the scripts of that year.

## Preparing for a day

To be able to download the input data you need to have your session cookie stored in a file with the name `session_cookie.txt` in the root of this repository.
You can get your current cookie from the website while being logged in.
Remember that it expires after some time.

Run `prepare.py` to download the input and generate the script and tests from templates for the current day.
The optional arguments are `year` and `day` with the current year and day as default values.
Run `prepare.py --all-inputs` to download all inputs you don't yet have.

## Running the scripts

Run `aoc.py` to run the script for the current day. Use the arguments `year` and `day` to specify a different date.
For example, `python aoc.py 2021 10` runs Advent of Code 2021-12-10.

## Testing

Run `test.py` to run all tests in the `test` directory.
Use the optional arguments `year` and `day` to run only one year or only one day from that year.
With `--skip-samples` the scripts are only checked against the real inputs.
With `--verbosity` followed by an integer you can control the amount of `unittest` output.
`0` is quiet, `1` is just the dots (default), and `2` is verbose.
