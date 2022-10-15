import os

from src.util.types import Data


def load_data(year: int, day: int) -> Data:
    # This way of resolving the path makes it easier to run the tests from the ide.
    this_path = os.path.dirname(os.path.realpath(__file__))
    year_directory = os.path.abspath(f"{this_path}/../../input/{year}")
    day_padded = str(day).zfill(2)
    filenames = [name for name in os.listdir(year_directory) if name.startswith(day_padded)]

    data = Data()
    for filename in sorted(filenames):
        path = year_directory + "/" + filename
        with open(path) as file:
            data_str = file.read().strip()
        if filename.endswith("input.txt"):
            data.input = data_str
        else:
            data.samples.append(data_str)
    return data
