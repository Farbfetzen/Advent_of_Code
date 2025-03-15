import os

from src.util.types import Inputs


def load_inputs(year: int, day: int) -> Inputs:
    # This way of resolving the path makes it easier to run the tests from the ide.
    this_path = os.path.dirname(os.path.realpath(__file__))
    year_directory = os.path.abspath(f"{this_path}/../../../input/{year}")
    day_padded = str(day).zfill(2)
    filenames = [name for name in os.listdir(year_directory) if name.startswith(day_padded)]

    inputs = Inputs()
    for filename in sorted(filenames):
        path = year_directory + "/" + filename
        with open(path) as file:
            content = file.read().strip()
        if filename.endswith("input.txt"):
            inputs.input = content
        else:
            inputs.samples.append(content)
    return inputs
