from src import solutions
from src.util.inputs import load_inputs


def test_day_01() -> None:
    solution = solutions[2020][1]()
    solution.solve(load_inputs(2020, 1))
    assert solution.sample_results_1[0] == 514579
    assert solution.sample_results_2[0] == 241861950
    assert solution.result_1 == 436404
    assert solution.result_2 == 274879808


def test_day_02() -> None:
    solution = solutions[2020][2]()
    solution.solve(load_inputs(2020, 2))
    assert solution.sample_results_1[0] == 2
    assert solution.sample_results_2[0] == 1
    assert solution.result_1 == 434
    assert solution.result_2 == 509


def test_day_03() -> None:
    solution = solutions[2020][3]()
    solution.solve(load_inputs(2020, 3))
    assert solution.sample_results_1[0] == 7
    assert solution.result_1 == 211
    assert solution.result_2 == 3584591857


def test_day_04() -> None:
    solution = solutions[2020][4]()
    solution.solve(load_inputs(2020, 4))
    assert solution.sample_results_1[0] == 2
    assert solution.result_1 == 208
    assert solution.result_2 == 167


def test_day_05() -> None:
    solution = solutions[2020][5]()
    solution.solve(load_inputs(2020, 5))
    assert solution.sample_results_other["seat ids"] == [357, 567, 119, 820]
    assert solution.result_1 == 848
    assert solution.result_2 == 682


def test_day_06() -> None:
    solution = solutions[2020][6]()
    solution.solve(load_inputs(2020, 6))
    assert solution.sample_results_1[0] == 11
    assert solution.sample_results_2[0] == 6
    assert solution.result_1 == 6686
    assert solution.result_2 == 3476


def test_day_07() -> None:
    solution = solutions[2020][7]()
    solution.solve(load_inputs(2020, 7))
    assert solution.sample_results_1[0] == 4
    assert solution.sample_results_2[0] == 32
    assert solution.sample_results_2[1] == 126
    assert solution.result_1 == 348
    assert solution.result_2 == 18885


def test_day_08() -> None:
    solution = solutions[2020][8]()
    solution.solve(load_inputs(2020, 8))
    assert solution.sample_results_1[0] == 5
    assert solution.sample_results_2[0] == 8
    assert solution.result_1 == 1262
    assert solution.result_2 == 1643


def test_day_09() -> None:
    solution = solutions[2020][9]()
    solution.solve(load_inputs(2020, 9))
    assert solution.sample_results_1[0] == 127
    assert solution.sample_results_2[0] == 62
    assert solution.result_1 == 21806024
    assert solution.result_2 == 2986195


def test_day_10() -> None:
    solution = solutions[2020][10]()
    solution.solve(load_inputs(2020, 10))
    assert solution.sample_results_1[0] == 35
    assert solution.sample_results_1[1] == 220
    assert solution.sample_results_2[0] == 8
    assert solution.sample_results_2[1] == 19208
    assert solution.result_1 == 2760
    assert solution.result_2 == 13816758796288


def test_day_11() -> None:
    solution = solutions[2020][11]()
    solution.solve(load_inputs(2020, 11))
    assert solution.sample_results_1[0] == 37
    assert solution.sample_results_2[0] == 26
    assert solution.result_1 == 2299
    assert solution.result_2 == 2047


def test_day_12() -> None:
    solution = solutions[2020][12]()
    solution.solve(load_inputs(2020, 12))
    assert solution.sample_results_1[0] == 25
    assert solution.sample_results_2[0] == 286
    assert solution.result_1 == 362
    assert solution.result_2 == 29895


def test_day_13() -> None:
    solution = solutions[2020][13]()
    inputs = load_inputs(2020, 13)
    solution.solve(inputs)
    assert solution.sample_results_1[0] == 295
    assert solution.sample_results_2[0] == 1068781
    assert solution.solve_2_without_crt(solution.prepare(inputs.samples[0])) == 1068781
    assert solution.result_1 == 3882
    assert solution.result_2 == 867295486378319
    assert solution.solve_2_without_crt(solution.prepare(inputs.input)) == 867295486378319


def test_day_14() -> None:
    solution = solutions[2020][14]()
    solution.solve(load_inputs(2020, 14))
    assert solution.sample_results_1[0] == 165
    assert solution.sample_results_2[0] == 208
    assert solution.result_1 == 4297467072083
    assert solution.result_2 == 5030603328768


def test_day_15() -> None:
    solution = solutions[2020][15]()
    solution.solve(load_inputs(2020, 15))
    assert solution.result_1 == 240
    assert solution.result_2 == 505


def test_day_16() -> None:
    solution = solutions[2020][16]()
    solution.solve(load_inputs(2020, 16))
    assert solution.sample_results_1[0] == 71
    assert solution.result_1 == 27802
    assert solution.result_2 == 279139880759


def test_day_17() -> None:
    solution = solutions[2020][17]()
    solution.solve(load_inputs(2020, 17))
    assert solution.sample_results_1[0] == 112
    assert solution.sample_results_2[0] == 848
    assert solution.result_1 == 232
    assert solution.result_2 == 1620


def test_day_18() -> None:
    solution = solutions[2020][18]()
    solution.solve(load_inputs(2020, 18))
    assert solution.sample_results_1[0] == 71
    assert solution.sample_results_1[1] == 51
    assert solution.sample_results_1[2] == 26
    assert solution.sample_results_1[3] == 437
    assert solution.sample_results_1[4] == 12240
    assert solution.sample_results_1[5] == 13632
    assert solution.sample_results_2[0] == 231
    assert solution.sample_results_2[1] == 51
    assert solution.sample_results_2[2] == 46
    assert solution.sample_results_2[3] == 1445
    assert solution.sample_results_2[4] == 669060
    assert solution.sample_results_2[5] == 23340
    assert solution.result_1 == 25190263477788
    assert solution.result_2 == 297139939002972


def test_day_19() -> None:
    solution = solutions[2020][19]()
    solution.solve(load_inputs(2020, 19))
    assert solution.sample_results_1[0] == 2
    assert solution.sample_results_1[1] == 3
    assert solution.sample_results_2[0] == 12
    assert solution.result_1 == 248
    assert solution.result_2 == 381


def test_day_20() -> None:
    solution = solutions[2020][20]()
    solution.solve(load_inputs(2020, 20))
    assert solution.sample_results_1[0] == 20899048083289
    assert solution.sample_results_2[0] == 273
    assert solution.result_1 == 27798062994017
    assert solution.result_2 == 2366


def test_day_21() -> None:
    solution = solutions[2020][21]()
    solution.solve(load_inputs(2020, 21))
    assert solution.sample_results_1[0] == 5
    assert solution.sample_results_2[0] == "mxmxvkd,sqjhc,fvjkl"
    assert solution.result_1 == 2061
    assert solution.result_2 == "cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl"


def test_day_22() -> None:
    solution = solutions[2020][22]()
    solution.solve(load_inputs(2020, 22))
    assert solution.sample_results_1[0] == 306
    assert solution.sample_results_2[0] == 291
    assert solution.result_1 == 30138
    assert solution.result_2 == 31587


def test_day_23() -> None:
    solution = solutions[2020][23]()
    solution.solve(load_inputs(2020, 23))
    assert solution.sample_results_1[0] == 67384529
    assert solution.sample_results_2[0] == 149245887792
    assert solution.result_1 == 24798635
    assert solution.result_2 == 12757828710


def test_day_24() -> None:
    solution = solutions[2020][24]()
    solution.solve(load_inputs(2020, 24))
    assert solution.sample_results_1[0] == 10
    assert solution.sample_results_2[0] == 2208
    assert solution.result_1 == 528
    assert solution.result_2 == 4200


def test_day_25() -> None:
    solution = solutions[2020][25]()
    solution.solve(load_inputs(2020, 25))
    assert solution.sample_results_1[0] == 14897079
    assert solution.result_1 == 16902792
