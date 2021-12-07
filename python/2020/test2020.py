import unittest

import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25


class Test2020(unittest.TestCase):

    def test_01(self):
        sample_data = day01.get_data(day01.SAMPLE_PATH)
        self.assertEqual(day01.part_1(sample_data), 514579)
        self.assertEqual(day01.part_2(sample_data), 241861950)

        challenge_data = day01.get_data(day01.INPUT_PATH)
        self.assertEqual(day01.part_1(challenge_data), 436404)
        self.assertEqual(day01.part_2(challenge_data), 274879808)

    def test_02(self):
        sample_data = day02.get_data(day02.SAMPLE_PATH)
        self.assertEqual(day02.part_1(sample_data), 2)
        self.assertEqual(day02.part_2(sample_data), 1)

        challenge_data = day02.get_data(day02.INPUT_PATH)
        self.assertEqual(day02.part_1(challenge_data), 434)
        self.assertEqual(day02.part_2(challenge_data), 509)

    def test_03(self):
        sample_data = day03.get_data(day03.SAMPLE_PATH)
        self.assertEqual(day03.part_1(sample_data), 7)

        challenge_data = day03.get_data(day03.INPUT_PATH)
        self.assertEqual(day03.part_1(challenge_data), 211)
        self.assertEqual(day03.part_2(challenge_data), 3584591857)

    def test_04(self):
        sample_data = day04.get_data(day04.SAMPLE_PATH)
        self.assertEqual(day04.part_1(sample_data), 2)

        challenge_data = day04.get_data(day04.INPUT_PATH)
        self.assertEqual(day04.part_1(challenge_data), 208)
        self.assertEqual(day04.part_2(challenge_data), 167)

    def test_05(self):
        self.assertEqual(day05.get_seat_id(day05.SAMPLE_DATA[0]), 357)
        self.assertEqual(day05.get_seat_id(day05.SAMPLE_DATA[1]), 567)
        self.assertEqual(day05.get_seat_id(day05.SAMPLE_DATA[2]), 119)
        self.assertEqual(day05.get_seat_id(day05.SAMPLE_DATA[3]), 820)

        challenge_data = day05.get_data(day05.INPUT_PATH)
        self.assertEqual(day05.part_1(challenge_data), 848)
        self.assertEqual(day05.part_2(challenge_data), 682)

    def test_06(self):
        sample_data = day06.get_data(day06.SAMPLE_PATH)
        self.assertEqual(day06.part_1(sample_data), 11)
        self.assertEqual(day06.part_2(sample_data), 6)

        challenge_data = day06.get_data(day06.INPUT_PATH)
        self.assertEqual(day06.part_1(challenge_data), 6686)
        self.assertEqual(day06.part_2(challenge_data), 3476)

    def test_07(self):
        sample_data = day07.get_data(day07.SAMPLE_PATH)
        self.assertEqual(day07.part_1(sample_data[0]), 4)
        self.assertEqual(day07.part_2(sample_data[0]), 32)
        self.assertEqual(day07.part_2(sample_data[1]), 126)

        challenge_data = day07.get_data(day07.INPUT_PATH)[0]
        self.assertEqual(day07.part_1(challenge_data), 348)
        self.assertEqual(day07.part_2(challenge_data), 18885)

    def test_08(self):
        sample_data = day08.get_data(day08.SAMPLE_PATH)
        self.assertEqual(day08.part_1(sample_data), 5)
        self.assertEqual(day08.part_2(sample_data), 8)

        challenge_data = day08.get_data(day08.INPUT_PATH)
        self.assertEqual(day08.part_1(challenge_data), 1262)
        self.assertEqual(day08.part_2(challenge_data), 1643)

    def test_09(self):
        sample_data = day09.get_data(day09.SAMPLE_PATH)
        sample_invalid_number = day09.part_1(sample_data, 5)
        self.assertEqual(sample_invalid_number, 127)
        self.assertEqual(day09.part_2(sample_data, sample_invalid_number), 62)

        challenge_data = day09.get_data(day09.INPUT_PATH)
        challenge_invalid_number = day09.part_1(challenge_data, 25)
        self.assertEqual(challenge_invalid_number, 21806024)
        self.assertEqual(day09.part_2(challenge_data, challenge_invalid_number), 2986195)

    def test_10(self):
        sample_data = day10.get_data(day10.SAMPLE_PATH)
        self.assertEqual(day10.part_1(sample_data[0]), 35)
        self.assertEqual(day10.part_2(sample_data[0]), 8)
        self.assertEqual(day10.part_1(sample_data[1]), 220)
        self.assertEqual(day10.part_2(sample_data[1]), 19208)

        challenge_data = day10.get_data(day10.INPUT_PATH)[0]
        self.assertEqual(day10.part_1(challenge_data), 2760)
        self.assertEqual(day10.part_2(challenge_data), 13816758796288)

    def test_11(self):
        sample_data = day11.get_data(day11.SAMPLE_PATH)
        self.assertEqual(day11.part_1(sample_data), 37)
        self.assertEqual(day11.part_2(sample_data), 26)

        challenge_data = day11.get_data(day11.INPUT_PATH)
        self.assertEqual(day11.part_1(challenge_data), 2299)
        self.assertEqual(day11.part_2(challenge_data), 2047)

    def test_12(self):
        sample_data = day12.get_data(day12.SAMPLE_PATH)
        self.assertEqual(day12.navigate(sample_data, 1), 25)
        self.assertEqual(day12.navigate(sample_data, 2), 286)

        challenge_data = day12.get_data(day12.INPUT_PATH)
        self.assertEqual(day12.navigate(challenge_data, 1), 362)
        self.assertEqual(day12.navigate(challenge_data, 2), 29895)

    def test_13(self):
        sample_data = day13.get_data(day13.SAMPLE_PATH)
        self.assertEqual(day13.part_1(sample_data), 295)
        self.assertEqual(day13.part_2(sample_data), 1068781)
        self.assertEqual(day13.part_2(sample_data), 1068781)

        challenge_data = day13.get_data(day13.INPUT_PATH)
        self.assertEqual(day13.part_1(challenge_data), 3882)
        self.assertEqual(day13.part_2(challenge_data), 867295486378319)
        self.assertEqual(day13.part_2(challenge_data), 867295486378319)

    def test_14(self):
        sample_data = day14.get_data(day14.SAMPLE_PATH)
        self.assertEqual(day14.part_1(sample_data[0]), 165)
        self.assertEqual(day14.part_2(sample_data[1]), 208)

        challenge_data = day14.get_data(day14.INPUT_PATH)
        self.assertEqual(day14.part_1(challenge_data), 4297467072083)
        self.assertEqual(day14.part_2(challenge_data), 5030603328768)

    def test_15(self):
        challenge_data = day15.get_data(day15.INPUT_PATH)
        self.assertEqual(day15.play(challenge_data, 2020), 240)
        self.assertEqual(day15.play(challenge_data, 30_000_000), 505)

    def test_16(self):
        sample_data = day16.get_data(day16.SAMPLE_PATH)
        self.assertEqual(day16.part_1(sample_data), 71)

        challenge_data = day16.get_data(day16.INPUT_PATH)
        self.assertEqual(day16.part_1(challenge_data), 27802)
        self.assertEqual(day16.part_2(challenge_data), 279139880759)

    def test_17(self):
        sample_data = day17.get_data(day17.SAMPLE_PATH)
        self.assertEqual(day17.run_reactor(sample_data, 3), 112)
        self.assertEqual(day17.run_reactor(sample_data, 4), 848)

        challenge_data = day17.get_data(day17.INPUT_PATH)
        self.assertEqual(day17.run_reactor(challenge_data, 3), 232)
        self.assertEqual(day17.run_reactor(challenge_data, 4), 1620)

    def test_18(self):
        challenge_data = day18.get_data(day18.INPUT_PATH)[0]
        self.assertEqual(day18.part_1(challenge_data), 25190263477788)
        self.assertEqual(day18.part_2(challenge_data), 297139939002972)

    def test_19(self):
        sample_data = day19.get_data(day19.SAMPLE_PATH)
        self.assertEqual(day19.part_1(*sample_data[0]), 2)
        self.assertEqual(day19.part_1(*sample_data[1]), 3)
        self.assertEqual(day19.part_2(*sample_data[1]), 12)

        challenge_data = day19.get_data(day19.INPUT_PATH)[0]
        self.assertEqual(day19.part_1(*challenge_data), 248)
        self.assertEqual(day19.part_2(*challenge_data), 381)

    def test_20(self):
        sample_data = day20.get_data(day20.SAMPLE_PATH)
        self.assertEqual(day20.part_1(sample_data), 20899048083289)
        self.assertEqual(day20.part_2(sample_data), 273)

        challenge_data = day20.get_data(day20.INPUT_PATH)
        self.assertEqual(day20.part_1(challenge_data), 27798062994017)
        self.assertEqual(day20.part_2(challenge_data), 2366)

    def test_21(self):
        sample_data = day21.get_data(day21.SAMPLE_PATH)
        sample_sum_safe, sample_allergem_map = day21.part_1(sample_data)
        self.assertEqual(sample_sum_safe, 5)
        self.assertEqual(day21.part_2(sample_allergem_map), "mxmxvkd,sqjhc,fvjkl")

        challenge_data = day21.get_data(day21.INPUT_PATH)
        challenge_sum_safe, challenge_allergem_map = day21.part_1(challenge_data)
        self.assertEqual(challenge_sum_safe, 2061)
        self.assertEqual(
            day21.part_2(challenge_allergem_map),
            "cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl"
        )

    def test_22(self):
        sample_data = day22.get_data(day22.SAMPLE_PATH)
        self.assertEqual(day22.part_1(sample_data), 306)
        self.assertEqual(day22.part_2(sample_data), 291)

        challenge_data = day22.get_data(day22.INPUT_PATH)
        self.assertEqual(day22.part_1(challenge_data), 30138)
        self.assertEqual(day22.part_2(challenge_data), 31587)

    def test_23(self):
        sample_data = day23.get_data(day23.SAMPLE_PATH)
        self.assertEqual(day23.part_1(sample_data), "67384529")
        self.assertEqual(day23.part_2(sample_data), "149245887792")

        challenge_data = day23.get_data(day23.INPUT_PATH)
        self.assertEqual(day23.part_1(challenge_data), "24798635")
        self.assertEqual(day23.part_2(challenge_data), "12757828710")

    def test_24(self):
        sample_data = day24.get_data(day24.SAMPLE_PATH)
        sample_sum_black, sample_tiles = day24.part_1(sample_data)
        self.assertEqual(sample_sum_black, 10)
        self.assertEqual(day24.part_2(sample_tiles), 2208)

        challenge_data = day24.get_data(day24.INPUT_PATH)
        challenge_sum_black, challenge_tiles = day24.part_1(challenge_data)
        self.assertEqual(challenge_sum_black, 528)
        self.assertEqual(day24.part_2(challenge_tiles), 4200)

    def test_25(self):
        sample_data = day25.get_data(day25.SAMPLE_PATH)
        self.assertEqual(day25.part_1(sample_data), 14897079)

        challenge_data = day25.get_data(day25.INPUT_PATH)
        self.assertEqual(day25.part_1(challenge_data), 16902792)


if __name__ == "__main__":
    unittest.main()
