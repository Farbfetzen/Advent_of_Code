from src import solutions
from src.util.inputs import load_inputs


def test_day_01() -> None:
    solution = solutions[2022][1]()
    solution.solve(load_inputs(2022, 1))
    assert solution.sample_results_1[0] == 24000
    assert solution.sample_results_2[0] == 45000
    assert solution.result_1 == 68923
    assert solution.result_2 == 200044


def test_day_02() -> None:
    solution = solutions[2022][2]()
    solution.solve(load_inputs(2022, 2))
    assert solution.sample_results_1[0] == 15
    assert solution.sample_results_2[0] == 12
    assert solution.result_1 == 13682
    assert solution.result_2 == 12881


def test_day_03() -> None:
    solution = solutions[2022][3]()
    solution.solve(load_inputs(2022, 3))
    assert solution.sample_results_1[0] == 157
    assert solution.sample_results_2[0] == 70
    assert solution.result_1 == 7766
    assert solution.result_2 == 2415


def test_day_04() -> None:
    solution = solutions[2022][4]()
    solution.solve(load_inputs(2022, 4))
    assert solution.sample_results_1[0] == 2
    assert solution.sample_results_2[0] == 4
    assert solution.result_1 == 496
    assert solution.result_2 == 847
