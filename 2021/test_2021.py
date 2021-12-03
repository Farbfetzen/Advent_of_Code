import unittest

import day_01
import day_02
import day_03


class Test2021(unittest.TestCase):

    def test_01(self):
        self.assertEqual(day_01.part_1(day_01.sample_data), 7)
        self.assertEqual(day_01.part_2(day_01.sample_data), 5)

        self.assertEqual(day_01.part_1(day_01.challenge_data), 1766)
        self.assertEqual(day_01.part_2(day_01.challenge_data), 1797)

    def test_02(self):
        hda_sample = day_02.follow_course(day_02.sample_data)
        self.assertEqual(day_02.part_1(*hda_sample), 150)
        self.assertEqual(day_02.part_2(*hda_sample), 900)

        hda_challenge = day_02.follow_course(day_02.challenge_data)
        self.assertEqual(day_02.part_1(*hda_challenge), 2073315)
        self.assertEqual(day_02.part_2(*hda_challenge), 1840311528)
        
    def test_03(self):
        self.assertEqual(day_03.part_1(day_03.sample_data), 198)
        self.assertEqual(day_03.part_2(day_03.sample_data), 230)

        self.assertEqual(day_03.part_1(day_03.challenge_data), 693486)
        self.assertEqual(day_03.part_2(day_03.challenge_data), 3379326)


if __name__ == "__main__":
    unittest.main()
