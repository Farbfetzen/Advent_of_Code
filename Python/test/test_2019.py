from src import solutions
from src.util.inputs import load_inputs
from src.year_2019 import Solution2019Day04


def test_day_01() -> None:
    solution = solutions[2019][1]()
    solution.solve(load_inputs(2019, 1))
    assert solution.sample_results_1[0] == 34241
    assert solution.sample_results_2[0] == 51316
    assert solution.result_1 == 3223398
    assert solution.result_2 == 4832253


def test_day_03() -> None:
    solution = solutions[2019][3]()
    solution.solve(load_inputs(2019, 3))
    assert solution.sample_results_1[0] == 159
    assert solution.sample_results_1[1] == 135
    assert solution.sample_results_2[0] == 610
    assert solution.sample_results_2[1] == 410
    assert solution.result_1 == 489
    assert solution.result_2 == 93654


def test_day_04() -> None:
    solution: Solution2019Day04 = solutions[2019][4]()
    assert solution.check_increasing_digits("111111")
    assert solution.check_adjacent_pairs("111111")
    assert not solution.check_increasing_digits("223450")
    assert solution.check_adjacent_pairs("223450")
    assert solution.check_increasing_digits("123789")
    assert not solution.check_adjacent_pairs("123789")
    assert solution.check_increasing_digits("112233")
    assert solution.check_adjacent_pairs_group("112233")
    assert solution.check_increasing_digits("123444")
    assert not solution.check_adjacent_pairs_group("123444")
    assert solution.check_increasing_digits("111122")
    assert solution.check_adjacent_pairs_group("111122")

    solution.solve(load_inputs(2019, 4))
    assert solution.result_1 == 1650
    assert solution.result_2 == 1129


def test_day_06() -> None:
    solution = solutions[2019][6]()
    solution.solve(load_inputs(2019, 6))
    assert solution.sample_results_1[0] == 42
    assert solution.sample_results_2[0] == 4
    assert solution.result_1 == 253104
    assert solution.result_2 == 499


def test_day_08() -> None:
    solution = solutions[2019][8]()
    solution.solve(load_inputs(2019, 8))
    assert solution.sample_results_1[0] == 1
    assert solution.sample_results_2[0] == (
        " █\n"
        "█ "
    )
    assert solution.result_1 == 2520
    assert solution.result_2 == (
        "█    ████  ██    ██ █   █\n"
        "█    █    █  █    █ █   █\n"
        "█    ███  █       █  █ █ \n"
        "█    █    █ ██    █   █  \n"
        "█    █    █  █ █  █   █  \n"
        "████ ████  ███  ██    █  "
    )


def test_day_10() -> None:
    solution = solutions[2019][10]()
    solution.solve(load_inputs(2019, 10))
    assert solution.sample_results_1[0] == 210
    assert solution.sample_results_2[0] == 802
    assert solution.result_1 == 221
    assert solution.result_2 == 806


def test_day_12() -> None:
    solution = solutions[2019][12]()
    solution.solve(load_inputs(2019, 12))
    assert solution.sample_results_1[0] == 179
    assert solution.sample_results_1[1] == 1940
    assert solution.sample_results_2[0] == 2772
    assert solution.sample_results_2[1] == 4686774924
    assert solution.result_1 == 8742
    assert solution.result_2 == 325433763467176


def test_day_14() -> None:
    solution = solutions[2019][14]()
    solution.solve(load_inputs(2019, 14))
    assert solution.sample_results_1[0] == 13312
    assert solution.sample_results_1[1] == 180697
    assert solution.sample_results_1[2] == 2210736
    assert solution.sample_results_2[0] == 82892753
    assert solution.sample_results_2[1] == 5586022
    assert solution.sample_results_2[2] == 460664
    assert solution.result_1 == 907302
    assert solution.result_2 == 1670299


def test_day_16() -> None:
    solution = solutions[2019][16]()
    solution.solve(load_inputs(2019, 16))
    assert solution.sample_results_1[0] == "24176176"
    assert solution.sample_results_1[1] == "73745418"
    assert solution.sample_results_1[2] == "52432133"
    assert solution.sample_results_2[0] == "84462026"
    assert solution.sample_results_2[1] == "78725270"
    assert solution.sample_results_2[2] == "53553731"
    assert solution.result_1 == "74608727"
    assert solution.result_2 == "57920757"


def test_day_18() -> None:
    solution = solutions[2019][18]()
    solution.solve(load_inputs(2019, 18))
    assert solution.sample_results_1[0] == 8
    assert solution.sample_results_1[1] == 86
    assert solution.sample_results_1[2] == 132
    assert solution.sample_results_1[3] == 136
    assert solution.sample_results_1[4] == 81
    assert solution.sample_results_2[0] == 8
    assert solution.sample_results_2[1] == 24
    assert solution.sample_results_2[2] == 32
    assert solution.sample_results_2[3] == 72
    assert solution.result_1 == 4406
    assert solution.result_2 == 1964


def test_day_20() -> None:
    solution = solutions[2019][20]()
    solution.solve(load_inputs(2019, 20))
    assert solution.sample_results_1[0] == 23
    assert solution.sample_results_1[1] == 58
    assert solution.sample_results_2[0] == 396
    assert solution.result_1 == 422
    assert solution.result_2 == 5040


def test_day_22() -> None:
    solution = solutions[2019][22]()
    solution.solve(load_inputs(2019, 22))
    assert solution.sample_results_other[0] == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    assert solution.sample_results_other[1] == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    assert solution.sample_results_other[2] == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
    assert solution.sample_results_other[3] == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
    assert solution.result_1 == 2480
    assert solution.result_2 == 62416301438548
