from src import solutions
from src.util.inputs import load_inputs


def test_day_01() -> None:
    solution = solutions[2021][1]()
    solution.solve(load_inputs(2021, 1))
    assert solution.sample_results_1[0] == 7
    assert solution.sample_results_2[0] == 5
    assert solution.result_1 == 1766
    assert solution.result_2 == 1797


def test_day_02() -> None:
    solution = solutions[2021][2]()
    solution.solve(load_inputs(2021, 2))
    assert solution.sample_results_1[0] == 150
    assert solution.sample_results_2[0] == 900
    assert solution.result_1 == 2073315
    assert solution.result_2 == 1840311528


def test_day_03() -> None:
    solution = solutions[2021][3]()
    solution.solve(load_inputs(2021, 3))
    assert solution.sample_results_1[0] == 198
    assert solution.sample_results_2[0] == 230
    assert solution.result_1 == 693486
    assert solution.result_2 == 3379326


def test_day_04() -> None:
    solution = solutions[2021][4]()
    solution.solve(load_inputs(2021, 4))
    assert solution.sample_results_1[0] == 4512
    assert solution.sample_results_2[0] == 1924
    assert solution.result_1 == 23177
    assert solution.result_2 == 6804


def test_day_05() -> None:
    solution = solutions[2021][5]()
    solution.solve(load_inputs(2021, 5))
    assert solution.sample_results_1[0] == 5
    assert solution.sample_results_2[0] == 12
    assert solution.result_1 == 6267
    assert solution.result_2 == 20196


def test_day_06() -> None:
    solution = solutions[2021][6]()
    solution.solve(load_inputs(2021, 6))
    assert solution.sample_results_1[0] == 5934
    assert solution.sample_results_2[0] == 26984457539
    assert solution.result_1 == 372300
    assert solution.result_2 == 1675781200288


def test_day_07() -> None:
    solution = solutions[2021][7]()
    solution.solve(load_inputs(2021, 7))
    assert solution.sample_results_1[0] == 37
    assert solution.sample_results_2[0] == 168
    assert solution.result_1 == 352331
    assert solution.result_2 == 99266250


def test_day_08() -> None:
    solution = solutions[2021][8]()
    solution.solve(load_inputs(2021, 8))
    assert solution.sample_results_1[0] == 26
    assert solution.sample_results_2[0] == 61229
    assert solution.result_1 == 352
    assert solution.result_2 == 936117


def test_day_09() -> None:
    solution = solutions[2021][9]()
    solution.solve(load_inputs(2021, 9))
    assert solution.sample_results_1[0] == 15
    assert solution.sample_results_2[0] == 1134
    assert solution.result_1 == 554
    assert solution.result_2 == 1017792


def test_day_10() -> None:
    solution = solutions[2021][10]()
    solution.solve(load_inputs(2021, 10))
    assert solution.sample_results_1[0] == 26397
    assert solution.sample_results_2[0] == 288957
    assert solution.result_1 == 362271
    assert solution.result_2 == 1698395182


def test_day_11() -> None:
    solution = solutions[2021][11]()
    solution.solve(load_inputs(2021, 11))
    assert solution.sample_results_1[0] == 1656
    assert solution.sample_results_2[0] == 195
    assert solution.result_1 == 1721
    assert solution.result_2 == 298


def test_day_12() -> None:
    solution = solutions[2021][12]()
    solution.solve(load_inputs(2021, 12))
    assert solution.sample_results_1[0] == 10
    assert solution.sample_results_1[1] == 19
    assert solution.sample_results_1[2] == 226
    assert solution.sample_results_2[0] == 36
    assert solution.sample_results_2[1] == 103
    assert solution.sample_results_2[2] == 3509
    assert solution.result_1 == 5920
    assert solution.result_2 == 155477


def test_day_13() -> None:
    solution = solutions[2021][13]()
    solution.solve(load_inputs(2021, 13))
    assert solution.sample_results_1[0] == 17
    expected_sample_2 = (
        "█████\n"
        "█   █\n"
        "█   █\n"
        "█   █\n"
        "█████"
    )
    assert solution.sample_results_2[0] == expected_sample_2
    assert solution.result_1 == 807
    expected_result_2 = (
        "█     ██  █  █ ████  ██  █  █ ████   ██\n"
        "█    █  █ █  █ █    █  █ █  █ █       █\n"
        "█    █    ████ ███  █    █  █ ███     █\n"
        "█    █ ██ █  █ █    █ ██ █  █ █       █\n"
        "█    █  █ █  █ █    █  █ █  █ █    █  █\n"
        "████  ███ █  █ ████  ███  ██  ████  ██ "
    )
    assert solution.result_2 == expected_result_2


def test_day_14() -> None:
    solution = solutions[2021][14]()
    solution.solve(load_inputs(2021, 14))
    assert solution.sample_results_1[0] == 1588
    assert solution.sample_results_2[0] == 2188189693529
    assert solution.result_1 == 2768
    assert solution.result_2 == 2914365137499


def test_day_15() -> None:
    solution = solutions[2021][15]()
    solution.solve(load_inputs(2021, 15))
    assert solution.sample_results_1[0] == 40
    assert solution.sample_results_2[0] == 315
    assert solution.result_1 == 717
    assert solution.result_2 == 2993


def test_day_16() -> None:
    solution = solutions[2021][16]()
    solution.solve(load_inputs(2021, 16))
    assert solution.sample_results_1[0] == 16
    assert solution.sample_results_1[1] == 12
    assert solution.sample_results_1[2] == 23
    assert solution.sample_results_1[3] == 31
    assert solution.sample_results_2[0] == 3
    assert solution.sample_results_2[1] == 54
    assert solution.sample_results_2[2] == 7
    assert solution.sample_results_2[3] == 9
    assert solution.sample_results_2[4] == 1
    assert solution.sample_results_2[5] == 0
    assert solution.sample_results_2[6] == 0
    assert solution.sample_results_2[7] == 1
    assert solution.result_1 == 940
    assert solution.result_2 == 13476220616073


def test_day_17() -> None:
    solution = solutions[2021][17]()
    solution.solve(load_inputs(2021, 17))
    assert solution.sample_results_1[0] == 45
    assert solution.sample_results_2[0] == 112
    assert solution.result_1 == 17766
    assert solution.result_2 == 1733


def test_day_18() -> None:
    solution = solutions[2021][18]()
    solution.solve(load_inputs(2021, 18))
    assert solution.sample_results_1[0] == 4140
    assert solution.sample_results_2[0] == 3993
    assert solution.result_1 == 3987
    assert solution.result_2 == 4500


def test_day_19() -> None:
    solution = solutions[2021][19]()
    solution.solve(load_inputs(2021, 19))
    assert solution.sample_results_1[0] == 79
    assert solution.sample_results_2[0] == 3621
    assert solution.result_1 == 451
    assert solution.result_2 == 13184


def test_day_20() -> None:
    solution = solutions[2021][20]()
    solution.solve(load_inputs(2021, 20))
    assert solution.sample_results_1[0] == 35
    assert solution.sample_results_2[0] == 3351
    assert solution.result_1 == 5081
    assert solution.result_2 == 15088


def test_day_21() -> None:
    solution = solutions[2021][21]()
    solution.solve(load_inputs(2021, 21))
    assert solution.sample_results_1[0] == 739785
    assert solution.sample_results_2[0] == 444356092776315
    assert solution.result_1 == 752247
    assert solution.result_2 == 221109915584112


def test_day_22() -> None:
    solution = solutions[2021][22]()
    solution.solve(load_inputs(2021, 22))
    assert solution.sample_results_1[0] == 39
    assert solution.sample_results_1[1] == 590784
    assert solution.sample_results_1[2] == 474140
    assert solution.sample_results_2[0] == 2758514936282235
    assert solution.result_1 == 620241
    assert solution.result_2 == 1284561759639324


def test_day_23() -> None:
    solution = solutions[2021][23]()
    solution.solve(load_inputs(2021, 23))
    assert solution.sample_results_1[0] == 12521
    assert solution.sample_results_2[0] == 44169
    assert solution.result_1 == 12240
    assert solution.result_2 == 44618


def test_day_24() -> None:
    solution = solutions[2021][24]()
    solution.solve(load_inputs(2021, 24))
    assert solution.result_1 == "29991993698469"
    assert solution.result_2 == "14691271141118"


def test_day_25() -> None:
    solution = solutions[2021][25]()
    solution.solve(load_inputs(2021, 25))
    assert solution.sample_results_1[0] == 58
    assert solution.result_1 == 532
