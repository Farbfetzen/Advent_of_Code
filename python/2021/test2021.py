import unittest

import day01
import day02
import day03
import day04
import day05
import day06
import day07


class Test2021(unittest.TestCase):

    def test_01(self):
        self.assertEqual(day01.part_1(day01.sample_data), 7)
        self.assertEqual(day01.part_2(day01.sample_data), 5)

        self.assertEqual(day01.part_1(day01.challenge_data), 1766)
        self.assertEqual(day01.part_2(day01.challenge_data), 1797)

    def test_02(self):
        hda_sample = day02.follow_course(day02.sample_data)
        self.assertEqual(day02.part_1(*hda_sample), 150)
        self.assertEqual(day02.part_2(*hda_sample), 900)

        hda_challenge = day02.follow_course(day02.challenge_data)
        self.assertEqual(day02.part_1(*hda_challenge), 2073315)
        self.assertEqual(day02.part_2(*hda_challenge), 1840311528)
        
    def test_03(self):
        self.assertEqual(day03.part_1(day03.sample_data), 198)
        self.assertEqual(day03.part_2(day03.sample_data), 230)

        self.assertEqual(day03.part_1(day03.challenge_data), 693486)
        self.assertEqual(day03.part_2(day03.challenge_data), 3379326)

    def test_04(self):
        sample_part_1, sample_part_2 = day04.play(*day04.sample_data)
        self.assertEqual(sample_part_1, 4512)
        self.assertEqual(sample_part_2, 1924)

        challenge_part_1, challenge_part_2 = day04.play(*day04.challenge_data)
        self.assertEqual(challenge_part_1, 23177)
        self.assertEqual(challenge_part_2, 6804)
        
    def test_05(self):
        self.assertEqual(day05.part_1(day05.sample_data), 5)
        self.assertEqual(day05.part_2(day05.sample_data), 12)

        self.assertEqual(day05.part_1(day05.challenge_data), 6267)
        self.assertEqual(day05.part_2(day05.challenge_data), 20196)
        
    def test_06(self):
        sample_part_1, sample_part_2 = day06.simulate(day06.sample_data)
        self.assertEqual(sample_part_1, 5934)
        self.assertEqual(sample_part_2, 26984457539)

        challenge_part_1, challenge_part_2 = day06.simulate(day06.challenge_data)
        self.assertEqual(challenge_part_1, 372300)
        self.assertEqual(challenge_part_2, 1675781200288)

    def test_07(self):
        sample_data = day07.get_data(day07.SAMPLE_PATH)
        self.assertEqual(day07.part_1(sample_data), 37)
        self.assertEqual(day07.part_2(sample_data), 168)

        challenge_data = day07.get_data(day07.INPUT_PATH)
        self.assertEqual(day07.part_1(challenge_data), 352331)
        self.assertEqual(day07.part_2(challenge_data), 99266250)


if __name__ == "__main__":
    unittest.main()
