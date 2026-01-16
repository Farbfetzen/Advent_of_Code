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


def test_day_02() -> None:
    solution = solutions[2019][2]()
    solution.solve(load_inputs(2019, 2))
    assert solution.sample_results_other["sample 0"] == (3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50)
    assert solution.sample_results_other["sample 1"] == (2, 0, 0, 0, 99)
    assert solution.sample_results_other["sample 2"] == (2, 3, 0, 6, 99)
    assert solution.sample_results_other["sample 3"] == (2, 4, 4, 5, 99, 9801)
    assert solution.sample_results_other["sample 4"] == (30, 1, 1, 4, 2, 5, 6, 0, 99)
    assert solution.result_1 == 3101844
    assert solution.result_2 == 8478


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


def test_day_05() -> None:
    solution = solutions[2019][5]()
    solution.solve(load_inputs(2019, 5))
    assert solution.result_1 == 9006673
    assert solution.result_2 == 3629692


def test_day_06() -> None:
    solution = solutions[2019][6]()
    solution.solve(load_inputs(2019, 6))
    assert solution.sample_results_1[0] == 42
    assert solution.sample_results_2[0] == 4
    assert solution.result_1 == 253104
    assert solution.result_2 == 499


def test_day_07() -> None:
    solution = solutions[2019][7]()
    solution.solve(load_inputs(2019, 7))
    assert solution.sample_results_1[0] == 43210
    assert solution.sample_results_1[1] == 54321
    assert solution.sample_results_1[2] == 65210
    assert solution.sample_results_2[0] == 139629729
    assert solution.sample_results_2[1] == 18216
    assert solution.result_1 == 21000
    assert solution.result_2 == 61379886


def test_day_08() -> None:
    solution = solutions[2019][8]()
    solution.solve(load_inputs(2019, 8))
    assert solution.sample_results_1[0] == 1
    # fmt: off
    assert solution.sample_results_2[0] == (
        " █\n"
        "█ "
    )
    # fmt: on
    assert solution.result_1 == 2520
    assert solution.result_2 == (
        "█    ████  ██    ██ █   █\n"
        "█    █    █  █    █ █   █\n"
        "█    ███  █       █  █ █ \n"
        "█    █    █ ██    █   █  \n"
        "█    █    █  █ █  █   █  \n"
        "████ ████  ███  ██    █  "
    )


def test_day_09() -> None:
    solution = solutions[2019][9]()
    solution.solve(load_inputs(2019, 9))
    # fmt: off
    assert solution.sample_results_other["copy program"] == [109, 1, 204, -1, 1001, 100, 1, 100,
                                                             1008, 100, 16, 101, 1006, 101, 0, 99]
    # fmt: on
    assert len(str(solution.sample_results_1[0])) == 16
    assert solution.sample_results_1[1] == 1125899906842624
    assert solution.result_1 == 2457252183
    assert solution.result_2 == 70634


def test_day_10() -> None:
    solution = solutions[2019][10]()
    solution.solve(load_inputs(2019, 10))
    assert solution.sample_results_1[0] == 210
    assert solution.sample_results_2[0] == 802
    assert solution.result_1 == 221
    assert solution.result_2 == 806


def test_day_11() -> None:
    solution = solutions[2019][11]()
    solution.solve(load_inputs(2019, 11))
    assert solution.result_1 == 2428
    assert solution.result_2 == (
        " ███    ██ █    ████ ███  █  █  ██  █  █   \n"
        " █  █    █ █    █    █  █ █  █ █  █ █  █   \n"
        " █  █    █ █    ███  ███  █  █ █    █  █   \n"
        " ███     █ █    █    █  █ █  █ █    █  █   \n"
        " █ █  █  █ █    █    █  █ █  █ █  █ █  █   \n"
        " █  █  ██  ████ █    ███   ██   ██   ██    "
    )


def test_day_12() -> None:
    solution = solutions[2019][12]()
    solution.solve(load_inputs(2019, 12))
    assert solution.sample_results_1[0] == 179
    assert solution.sample_results_1[1] == 1940
    assert solution.sample_results_2[0] == 2772
    assert solution.sample_results_2[1] == 4686774924
    assert solution.result_1 == 8742
    assert solution.result_2 == 325433763467176


def test_day_13() -> None:
    solution = solutions[2019][13]()
    solution.solve(load_inputs(2019, 13))
    assert solution.result_1 == 268
    assert solution.result_2 == 13989


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


def test_day_15() -> None:
    solution = solutions[2019][15]()
    solution.solve(load_inputs(2019, 15))
    assert solution.result_1 == 330
    assert solution.result_2 == 352


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


def test_day_17() -> None:
    solution = solutions[2019][17]()
    solution.solve(load_inputs(2019, 17))
    assert solution.result_1 == 8520
    assert solution.result_2 == 926819


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


def test_day_19() -> None:
    solution = solutions[2019][19]()
    solution.solve(load_inputs(2019, 19))
    assert solution.result_1 == 173
    assert solution.result_2 == 6671097


def test_day_20() -> None:
    solution = solutions[2019][20]()
    solution.solve(load_inputs(2019, 20))
    assert solution.sample_results_1[0] == 23
    assert solution.sample_results_1[1] == 58
    assert solution.sample_results_2[0] == 26
    assert solution.sample_results_2[1] == 396
    assert solution.result_1 == 422
    assert solution.result_2 == 5040


def test_day_21() -> None:
    solution = solutions[2019][21]()
    solution.solve(load_inputs(2019, 21))
    assert solution.result_1 == 19362259
    assert solution.result_2 == 1141066762


def test_day_22() -> None:
    solution = solutions[2019][22]()
    solution.solve(load_inputs(2019, 22))
    assert solution.sample_results_other[0] == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    assert solution.sample_results_other[1] == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    assert solution.sample_results_other[2] == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
    assert solution.sample_results_other[3] == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
    assert solution.result_1 == 2480
    assert solution.result_2 == 62416301438548
