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


class Test2021(unittest.TestCase):

    def test_01(self):
        sample_data = day01.get_data(day01.SAMPLE_PATH)
        self.assertEqual(day01.part_1(sample_data), 7)
        self.assertEqual(day01.part_2(sample_data), 5)

        challenge_data = day01.get_data(day01.INPUT_PATH)
        self.assertEqual(day01.part_1(challenge_data), 1766)
        self.assertEqual(day01.part_2(challenge_data), 1797)

    def test_02(self):
        sample_data = day02.get_data(day02.SAMPLE_PATH)
        hda_sample = day02.follow_course(sample_data)
        self.assertEqual(day02.part_1(*hda_sample), 150)
        self.assertEqual(day02.part_2(*hda_sample), 900)

        challenge_data = day02.get_data(day02.INPUT_PATH)
        hda_challenge = day02.follow_course(challenge_data)
        self.assertEqual(day02.part_1(*hda_challenge), 2073315)
        self.assertEqual(day02.part_2(*hda_challenge), 1840311528)
        
    def test_03(self):
        sample_data = day03.get_data(day03.SAMPLE_PATH)
        self.assertEqual(day03.part_1(sample_data), 198)
        self.assertEqual(day03.part_2(sample_data), 230)

        challenge_data = day03.get_data(day03.INPUT_PATH)
        self.assertEqual(day03.part_1(challenge_data), 693486)
        self.assertEqual(day03.part_2(challenge_data), 3379326)

    def test_04(self):
        sample_data = day04.get_data(day04.SAMPLE_PATH)
        sample_part_1, sample_part_2 = day04.play(*sample_data)
        self.assertEqual(sample_part_1, 4512)
        self.assertEqual(sample_part_2, 1924)

        challenge_data = day04.get_data(day04.INPUT_PATH)
        challenge_part_1, challenge_part_2 = day04.play(*challenge_data)
        self.assertEqual(challenge_part_1, 23177)
        self.assertEqual(challenge_part_2, 6804)
        
    def test_05(self):
        sample_data = day05.get_data(day05.SAMPLE_PATH)
        self.assertEqual(day05.part_1(sample_data), 5)
        self.assertEqual(day05.part_2(sample_data), 12)

        challenge_data = day05.get_data(day05.INPUT_PATH)
        self.assertEqual(day05.part_1(challenge_data), 6267)
        self.assertEqual(day05.part_2(challenge_data), 20196)
        
    def test_06(self):
        sample_data = day06.get_data(day06.SAMPLE_PATH)
        sample_part_1, sample_part_2 = day06.simulate(sample_data)
        self.assertEqual(sample_part_1, 5934)
        self.assertEqual(sample_part_2, 26984457539)

        challenge_data = day06.get_data(day06.INPUT_PATH)
        challenge_part_1, challenge_part_2 = day06.simulate(challenge_data)
        self.assertEqual(challenge_part_1, 372300)
        self.assertEqual(challenge_part_2, 1675781200288)

    def test_07(self):
        sample_data = day07.get_data(day07.SAMPLE_PATH)
        self.assertEqual(day07.part_1(sample_data), 37)
        self.assertEqual(day07.part_2(sample_data), 168)

        challenge_data = day07.get_data(day07.INPUT_PATH)
        self.assertEqual(day07.part_1(challenge_data), 352331)
        self.assertEqual(day07.part_2(challenge_data), 99266250)

    def test_08(self):
        sample_data = day08.get_data(day08.SAMPLE_PATH)
        self.assertEqual(day08.part_1(sample_data), 26)
        self.assertEqual(day08.part_2(sample_data), 61229)

        challenge_data = day08.get_data(day08.INPUT_PATH)
        self.assertEqual(day08.part_1(challenge_data), 352)
        self.assertEqual(day08.part_2(challenge_data), 936117)

    def test_09(self):
        sample_data = day09.get_data(day09.SAMPLE_PATH)
        self.assertEqual(day09.part_1(*sample_data), 15)
        self.assertEqual(day09.part_2(*sample_data), 1134)

        challenge_data = day09.get_data(day09.INPUT_PATH)
        self.assertEqual(day09.part_1(*challenge_data), 554)
        self.assertEqual(day09.part_2(*challenge_data), 1017792)

    def test_10(self):
        sample_data = day10.get_data(day10.SAMPLE_PATH)
        sample_part_1, sample_part_2 = day10.get_scores(sample_data)
        self.assertEqual(sample_part_1, 26397)
        self.assertEqual(sample_part_2, 288957)

        challenge_data = day10.get_data(day10.INPUT_PATH)
        challenge_part_1, challenge_part_2 = day10.get_scores(challenge_data)
        self.assertEqual(challenge_part_1, 362271)
        self.assertEqual(challenge_part_2, 1698395182)

    def test_11(self):
        octopuses_sample = day11.Octopuses(day11.SAMPLE_PATH)
        self.assertEqual(octopuses_sample.flashes_after_100_steps, 1656)
        self.assertEqual(octopuses_sample.steps, 195)

        octopuses_challenge = day11.Octopuses(day11.INPUT_PATH)
        self.assertEqual(octopuses_challenge.flashes_after_100_steps, 1721)
        self.assertEqual(octopuses_challenge.steps, 298)

    def test_12(self):
        sample_data = day12.get_data(day12.SAMPLE_PATH)
        self.assertEqual(day12.part_1(sample_data[0]), 10)
        self.assertEqual(day12.part_1(sample_data[1]), 19)
        self.assertEqual(day12.part_1(sample_data[2]), 226)
        self.assertEqual(day12.part_2(sample_data[0]), 36)
        self.assertEqual(day12.part_2(sample_data[1]), 103)
        self.assertEqual(day12.part_2(sample_data[2]), 3509)

        challenge_data = day12.get_data(day12.INPUT_PATH)[0]
        self.assertEqual(day12.part_1(challenge_data), 5920)
        self.assertEqual(day12.part_2(challenge_data), 155477)

    def test_13(self):
        sample_data = day13.get_data(day13.SAMPLE_PATH)
        self.assertEqual(day13.part_1(*sample_data), 17)
        self.assertEqual(day13.part_2(*sample_data), "█████\n█   █\n█   █\n█   █\n█████")

        challenge_data = day13.get_data(day13.INPUT_PATH)
        self.assertEqual(day13.part_1(*challenge_data), 807)
        expected_code = (
            "█     ██  █  █ ████  ██  █  █ ████   ██\n"
            "█    █  █ █  █ █    █  █ █  █ █       █\n"
            "█    █    ████ ███  █    █  █ ███     █\n"
            "█    █ ██ █  █ █    █ ██ █  █ █       █\n"
            "█    █  █ █  █ █    █  █ █  █ █    █  █\n"
            "████  ███ █  █ ████  ███  ██  ████  ██ "
        )
        self.assertEqual(day13.part_2(*challenge_data), expected_code)

    def test_14(self):
        sample_data = day14.get_data(day14.SAMPLE_PATH)
        self.assertEqual(day14.part_1(*sample_data), 1588)
        self.assertEqual(day14.part_2(*sample_data), 2188189693529)

        challenge_data = day14.get_data(day14.INPUT_PATH)
        self.assertEqual(day14.part_1(*challenge_data), 2768)
        self.assertEqual(day14.part_2(*challenge_data), 2914365137499)

    def test_15(self):
        sample_data = day15.get_data(day15.SAMPLE_PATH)
        self.assertEqual(day15.part_1(sample_data), 40)
        self.assertEqual(day15.part_2(sample_data), 315)

        challenge_data = day15.get_data(day15.INPUT_PATH)
        self.assertEqual(day15.part_1(challenge_data), 717)
        self.assertEqual(day15.part_2(challenge_data), 2993)

    def test_16(self):
        sample_data = day16.get_data(day16.SAMPLE_PATH)
        self.assertEqual(day16.part_1(sample_data[0]), 16)
        self.assertEqual(day16.part_1(sample_data[1]), 12)
        self.assertEqual(day16.part_1(sample_data[2]), 23)
        self.assertEqual(day16.part_1(sample_data[3]), 31)
        self.assertEqual(day16.part_2(sample_data[4]), 3)
        self.assertEqual(day16.part_2(sample_data[5]), 54)
        self.assertEqual(day16.part_2(sample_data[6]), 7)
        self.assertEqual(day16.part_2(sample_data[7]), 9)
        self.assertEqual(day16.part_2(sample_data[8]), 1)
        self.assertEqual(day16.part_2(sample_data[9]), 0)
        self.assertEqual(day16.part_2(sample_data[10]), 0)
        self.assertEqual(day16.part_2(sample_data[11]), 1)

        challenge_data = day16.get_data(day16.INPUT_PATH)[0]
        self.assertEqual(day16.part_1(challenge_data), 940)
        self.assertEqual(day16.part_2(challenge_data), 13476220616073)

    def test_17(self):
        sample_data = day17.get_data(day17.SAMPLE_PATH)
        self.assertEqual(day17.part_1(sample_data[2]), 45)
        self.assertEqual(day17.part_2(*sample_data), 112)

        challenge_data = day17.get_data(day17.INPUT_PATH)
        self.assertEqual(day17.part_1(challenge_data[2]), 17766)
        self.assertEqual(day17.part_2(*challenge_data), 1733)

    def test_18(self):
        sample_data = day18.get_data(day18.SAMPLE_PATH)
        self.assertEqual(day18.part_1(sample_data), 4140)
        self.assertEqual(day18.part_2(sample_data), 3993)

        challenge_data = day18.get_data(day18.INPUT_PATH)
        self.assertEqual(day18.part_1(challenge_data), 3987)
        self.assertEqual(day18.part_2(challenge_data), 4500)

    def test_19(self):
        sample_data = day19.get_data(day19.SAMPLE_PATH)
        self.assertEqual(day19.part_1(sample_data), 79)
        self.assertEqual(day19.part_2(sample_data), 3621)

        challenge_data = day19.get_data(day19.INPUT_PATH)
        self.assertEqual(day19.part_1(challenge_data), 451)
        self.assertEqual(day19.part_2(challenge_data), 13184)

    def test_20(self):
        sample_data = day20.get_data(day20.SAMPLE_PATH)
        self.assertEqual(day20.part_1(*sample_data), 35)
        self.assertEqual(day20.part_2(*sample_data), 3351)

        challenge_data = day20.get_data(day20.INPUT_PATH)
        self.assertEqual(day20.part_1(*challenge_data), 5081)
        self.assertEqual(day20.part_2(*challenge_data), 15088)

    def test_21(self):
        sample_data = day21.get_data(day21.SAMPLE_PATH)
        self.assertEqual(day21.part_1(*sample_data), 739785)
        self.assertEqual(day21.part_2(*sample_data), 444356092776315)

        challenge_data = day21.get_data(day21.INPUT_PATH)
        self.assertEqual(day21.part_1(*challenge_data), 752247)
        self.assertEqual(day21.part_2(*challenge_data), 221109915584112)

    def test_22(self):
        sample_data = day22.get_data(day22.SAMPLE_PATH)
        self.assertEqual(day22.part_1(sample_data[0]), 39)
        self.assertEqual(day22.part_1(sample_data[1]), 590784)
        self.assertEqual(day22.part_1(sample_data[2]), 474140)
        self.assertEqual(day22.part_2(sample_data[2]), 2758514936282235)

        challenge_data = day22.get_data(day22.INPUT_PATH)[0]
        self.assertEqual(day22.part_1(challenge_data), 620241)
        self.assertEqual(day22.part_2(challenge_data), 1284561759639324)


if __name__ == "__main__":
    unittest.main()
