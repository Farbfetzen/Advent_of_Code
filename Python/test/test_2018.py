from src import solutions
from src.util.inputs import load_inputs


def test_day_01() -> None:
    solution = solutions[2018][1]()
    solution.solve(load_inputs(2018, 1))
    assert solution.sample_results_1[0] == 3
    assert solution.sample_results_2[0] == 2
    assert solution.result_1 == 561
    assert solution.result_2 == 563


def test_day_02() -> None:
    solution = solutions[2018][2]()
    solution.solve(load_inputs(2018, 2))
    assert solution.sample_results_1[0] == 12
    assert solution.sample_results_2[0] == "fgij"
    assert solution.result_1 == 6696
    assert solution.result_2 == "bvnfawcnyoeyudzrpgslimtkj"


def test_day_03() -> None:
    solution = solutions[2018][3]()
    solution.solve(load_inputs(2018, 3))
    assert solution.sample_results_1[0] == 4
    assert solution.sample_results_2[0] == 3
    assert solution.result_1 == 104126
    assert solution.result_2 == 695


def test_day_04() -> None:
    solution = solutions[2018][4]()
    solution.solve(load_inputs(2018, 4))
    assert solution.sample_results_1[0] == 240
    assert solution.sample_results_2[0] == 4455
    assert solution.result_1 == 60438
    assert solution.result_2 == 47989
