from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Inputs:
    input: str = ""
    samples: list[str] = field(default_factory=lambda: [])


def load_inputs(year: int, day: int) -> Inputs:
    year_dir = Path(__file__).resolve().parents[3] / "input" / str(year)
    day_padded = str(day).zfill(2)
    inputs = Inputs()
    inputs.input = (year_dir / f"{day_padded}-input.txt").read_text().rstrip()
    sample_files = sorted(year_dir.glob(f"{day_padded}-sample*.txt"))
    for file in sample_files:
        inputs.samples.append(file.read_text().rstrip())
    return inputs
