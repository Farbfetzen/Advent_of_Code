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

This project uses [black](https://github.com/psf/black) for Python code formatting.

## Preparing for a day

Run `prepare.py` to download the input and generate the script and tests from templates for the current day.
The optional arguments are `year` and `day` with the current year and day as default values.

To be able to download the input data you need to have your session cookie stored as the `AOC_SESSION_COOKIE` environment variable .
You can get your current cookie from the website while being logged in.
Remember that it expires after some time.  
You also need to provide contact information in the User-Agent header of every request, so the maintainers of Advent of Code can contact you about the requests.
See [the automation rules](https://www.reddit.com/r/adventofcode/wiki/faqs/automation) in the subreddit and
[this post](https://www.reddit.com/r/adventofcode/comments/1pa472d/reminder_please_throttle_your_aoc_traffic/) by Eric Wastl.
To do this, set the environment variable `AOC_USER_AGENT` with your contact information, e.g. your email address.

I recomment putting the variables into an `.env` file and sourcing that:

```dotenv
export AOC_SESSION_COOKIE=123...
export AOC_USER_AGENT="foo@example.com, github.com/..."
```

## Running the scripts

Run `aoc.py` to run the script for the current day. Use the arguments `year` and `day` to specify a different date.
For example, `./aoc.py 2021 10` runs Advent of Code 2021-12-10.

## Testing

You can run `test.py` to run all tests in the `test` directory.
Use the optional arguments `year` and `day` to run only one year or only one day from that year.
The tests are run in parallel on all available cpu cores using [pytest-xdist](https://pytest-xdist.readthedocs.io) if more than one day is tested.
Of course, you can also run the tests using pytest directly, see [how-to-invoke-pytest](https://docs.pytest.org/en/stable/how-to/usage.html#how-to-invoke-pytest).
