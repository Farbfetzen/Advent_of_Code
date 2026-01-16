import os
import sys
from dataclasses import dataclass, field


@dataclass
class Inputs:
    input: str = ""
    samples: list[str] = field(default_factory=lambda: [])


def load_inputs(year: int, day: int) -> Inputs:
    # This way of resolving the path makes it easier to run the tests from the ide.
    this_path = os.path.dirname(os.path.realpath(__file__))
    year_directory = os.path.abspath(f"{this_path}/../../../input/{year}")
    day_padded = str(day).zfill(2)
    filenames = [name for name in os.listdir(year_directory) if name.startswith(day_padded)]
    input_filename = f"{day_padded}-input.txt"
    if input_filename not in filenames:
        sys.exit(f'File "{input_filename}" not in input directory!')

    inputs = Inputs()
    for filename in sorted(filenames):
        with open(f"{year_directory}/{filename}") as file:
            content = file.read().rstrip()
        if filename == input_filename:
            inputs.input = content
        elif filename.startswith(f"{day_padded}-sample"):
            inputs.samples.append(content)
        else:
            sys.exit(f'Unknown input file "{filename}".')
    return inputs
