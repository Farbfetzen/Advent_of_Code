# Python solutions for Advent of Code

Make sure this is the working directory for running the scripts because all paths and imports are relative to here.

## Setup

I recommend [virtualenv](https://virtualenv.pypa.io) for creating and managing the virtual environment.
The latest Python version with which the code was tested is 3.13.7.

```shell
virtualenv .venv -p python3.13
```

Activate the venv:

```shell
source .venv/bin/activate
```

Install the dependencies:

```shell
pip install -r requirements.txt
```

## Preparing for a day

To be able to download the input data you need to have your session cookie stored in a file with the name `session_cookie.txt` in the root of this repository.
You can get your current cookie from the website while being logged in.
Remember that it expires after some time.

Run `prepare.py` to download the input and generate the script and tests from templates for the current day.
The optional arguments are `year` and `day` with the current year and day as default values.
Run `prepare.py --all-inputs` to download all inputs you don't yet have.

## Running the scripts

Run `aoc.py` to run the script for the current day. Use the arguments `year` and `day` to specify a different date.
For example, `./aoc.py 2021 10` runs Advent of Code 2021-12-10.

## Testing

You can run `test.py` to run all tests in the `test` directory.
Use the optional arguments `year` and `day` to run only one year or only one day from that year.
The tests are run in parallel on all available cpu cores using [pytest-xdist](https://pytest-xdist.readthedocs.io) if more than one day is tested.
Of course, you can also run the tests using pytest directly, see [how-to-invoke-pytest](https://docs.pytest.org/en/stable/how-to/usage.html#how-to-invoke-pytest).
