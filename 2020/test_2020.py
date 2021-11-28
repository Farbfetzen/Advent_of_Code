import unittest

import day_01
import day_02
import day_03
import day_04
import day_05
import day_06
import day_07
import day_08
import day_09
import day_10
import day_11
import day_12
import day_13
import day_14
import day_15
import day_16
import day_17
import day_18
import day_19
import day_20
import day_21
import day_22
import day_23
import day_24
import day_25


class Test2020(unittest.TestCase):

    def test_01(self):
        self.assertEqual(day_01.part_1(day_01.sample_data), 514579)
        self.assertEqual(day_01.part_2(day_01.sample_data), 241861950)

        self.assertEqual(day_01.part_1(day_01.challenge_data), 436404)
        self.assertEqual(day_01.part_2(day_01.challenge_data), 274879808)

    def test_02(self):
        self.assertEqual(day_02.part_1(day_02.sample_data), 2)
        self.assertEqual(day_02.part_2(day_02.sample_data), 1)

        self.assertEqual(day_02.part_1(day_02.challenge_data), 434)
        self.assertEqual(day_02.part_2(day_02.challenge_data), 509)

    def test_03(self):
        self.assertEqual(day_03.part_1(day_03.sample_data), 7)

        self.assertEqual(day_03.part_1(day_03.challenge_data), 211)
        self.assertEqual(day_03.part_2(day_03.challenge_data), 3584591857)

    def test_04(self):
        self.assertEqual(day_04.part_1(day_04.sample_data), 2)

        self.assertEqual(day_04.part_1(day_04.challenge_data), 208)
        self.assertEqual(day_04.part_2(day_04.challenge_data), 167)

    def test_05(self):
        self.assertEqual(day_05.get_seat_id("FBFBBFFRLR"), 357)
        self.assertEqual(day_05.get_seat_id("BFFFBBFRRR"), 567)
        self.assertEqual(day_05.get_seat_id("FFFBBBFRRR"), 119)
        self.assertEqual(day_05.get_seat_id("BBFFBBFRLL"), 820)

        self.assertEqual(day_05.part_1(day_05.challenge_data), 848)
        self.assertEqual(day_05.part_2(day_05.challenge_data), 682)

    def test_06(self):
        self.assertEqual(day_06.part_1(day_06.sample_data), 11)
        self.assertEqual(day_06.part_2(day_06.sample_data), 6)

        self.assertEqual(day_06.part_1(day_06.challenge_data), 6686)
        self.assertEqual(day_06.part_2(day_06.challenge_data), 3476)

    def test_07(self):
        self.assertEqual(day_07.part_1(day_07.sample_data[0]), 4)
        self.assertEqual(day_07.part_2(day_07.sample_data[0]), 32)
        self.assertEqual(day_07.part_2(day_07.sample_data[1]), 126)

        self.assertEqual(day_07.part_1(day_07.challenge_data), 348)
        self.assertEqual(day_07.part_2(day_07.challenge_data), 18885)

    def test_08(self):
        self.assertEqual(day_08.part_1(day_08.sample_data), 5)
        self.assertEqual(day_08.part_2(day_08.sample_data), 8)

        self.assertEqual(day_08.part_1(day_08.challenge_data), 1262)
        self.assertEqual(day_08.part_2(day_08.challenge_data), 1643)

    def test_09(self):
        sample_invalid_number = day_09.part_1(day_09.sample_data, 5)
        self.assertEqual(sample_invalid_number, 127)
        self.assertEqual(day_09.part_2(day_09.sample_data, sample_invalid_number), 62)

        challenge_invalid_number = day_09.part_1(day_09.challenge_data, 25)
        self.assertEqual(challenge_invalid_number, 21806024)
        self.assertEqual(day_09.part_2(day_09.challenge_data, challenge_invalid_number), 2986195)

    def test_10(self):
        self.assertEqual(day_10.part_1(day_10.sample_data[0]), 35)
        self.assertEqual(day_10.part_2(day_10.sample_data[0]), 8)
        self.assertEqual(day_10.part_1(day_10.sample_data[1]), 220)
        self.assertEqual(day_10.part_2(day_10.sample_data[1]), 19208)

        self.assertEqual(day_10.part_1(day_10.challenge_data), 2760)
        self.assertEqual(day_10.part_2(day_10.challenge_data), 13816758796288)

    def test_11(self):
        self.assertEqual(day_11.part_1(day_11.sample_data), 37)
        self.assertEqual(day_11.part_2(day_11.sample_data), 26)

        self.assertEqual(day_11.part_1(day_11.challenge_data), 2299)
        self.assertEqual(day_11.part_2(day_11.challenge_data), 2047)

    def test_12(self):
        self.assertEqual(day_12.navigate(day_12.sample_data, 1), 25)
        self.assertEqual(day_12.navigate(day_12.sample_data, 2), 286)

        self.assertEqual(day_12.navigate(day_12.challenge_data, 1), 362)
        self.assertEqual(day_12.navigate(day_12.challenge_data, 2), 29895)

    def test_13(self):
        self.assertEqual(day_13.part_1(day_13.sample_data), 295)
        self.assertEqual(day_13.part_2(day_13.sample_data), 1068781)
        self.assertEqual(day_13.part_2(day_13.sample_data), 1068781)

        self.assertEqual(day_13.part_1(day_13.challenge_data), 3882)
        self.assertEqual(day_13.part_2(day_13.challenge_data), 867295486378319)
        self.assertEqual(day_13.part_2(day_13.challenge_data), 867295486378319)

    def test_14(self):
        self.assertEqual(day_14.part_1(day_14.sample_data[0]), 165)
        self.assertEqual(day_14.part_2(day_14.sample_data[1]), 208)

        self.assertEqual(day_14.part_1(day_14.challenge_data), 4297467072083)
        self.assertEqual(day_14.part_2(day_14.challenge_data), 5030603328768)

    def test_15(self):
        self.assertEqual(day_15.play(day_15.challenge_input, 2020), 240)
        self.assertEqual(day_15.play(day_15.challenge_input, 30_000_000), 505)

    def test_16(self):
        self.assertEqual(day_16.part_1(day_16.sample_data), 71)

        self.assertEqual(day_16.part_1(day_16.challenge_data), 27802)
        self.assertEqual(day_16.part_2(day_16.challenge_data), 279139880759)

    def test_17(self):
        self.assertEqual(day_17.run_reactor(day_17.sample_data, 3), 112)
        self.assertEqual(day_17.run_reactor(day_17.sample_data, 4), 848)

        self.assertEqual(day_17.run_reactor(day_17.challenge_data, 3), 232)
        self.assertEqual(day_17.run_reactor(day_17.challenge_data, 4), 1620)

    def test_18(self):
        self.assertEqual(day_18.part_1(day_18.challenge_data), 25190263477788)
        self.assertEqual(day_18.part_2(day_18.challenge_data), 297139939002972)

    def test_19(self):
        self.assertEqual(day_19.part_1(*day_19.sample_data[0]), 2)
        self.assertEqual(day_19.part_1(*day_19.sample_data[1]), 3)
        self.assertEqual(day_19.part_2(*day_19.sample_data[1]), 12)

        self.assertEqual(day_19.part_1(*day_19.challenge_data), 248)
        self.assertEqual(day_19.part_2(*day_19.challenge_data), 381)

    def test_20(self):
        self.assertEqual(day_20.part_1(day_20.sample_data), 20899048083289)
        self.assertEqual(day_20.part_2(day_20.sample_data), 273)

        self.assertEqual(day_20.part_1(day_20.challenge_data), 27798062994017)
        self.assertEqual(day_20.part_2(day_20.challenge_data), 2366)

    def test_21(self):
        sample_sum_safe, sample_allergem_map = day_21.part_1(day_21.sample_data)
        self.assertEqual(sample_sum_safe, 5)
        self.assertEqual(day_21.part_2(sample_allergem_map), "mxmxvkd,sqjhc,fvjkl")

        challenge_sum_safe, challenge_allergem_map = day_21.part_1(day_21.challenge_data)
        self.assertEqual(challenge_sum_safe, 2061)
        self.assertEqual(
            day_21.part_2(challenge_allergem_map),
            "cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl"
        )

    def test_22(self):
        self.assertEqual(day_22.part_1(day_22.sample_data), 306)
        self.assertEqual(day_22.part_2(day_22.sample_data), 291)

        self.assertEqual(day_22.part_1(day_22.challenge_data), 30138)
        self.assertEqual(day_22.part_2(day_22.challenge_data), 31587)

    def test_23(self):
        self.assertEqual(day_23.part_1(day_23.sample_data), "67384529")
        self.assertEqual(day_23.part_2(day_23.sample_data), "149245887792")

        self.assertEqual(day_23.part_1(day_23.challenge_data), "24798635")
        self.assertEqual(day_23.part_2(day_23.challenge_data), "12757828710")

    def test_24(self):
        sample_sum_black, sample_tiles = day_24.part_1(day_24.sample_data)
        self.assertEqual(sample_sum_black, 10)
        self.assertEqual(day_24.part_2(sample_tiles), 2208)

        challenge_sum_black, challenge_tiles = day_24.part_1(day_24.challenge_data)
        self.assertEqual(challenge_sum_black, 528)
        self.assertEqual(day_24.part_2(challenge_tiles), 4200)

    def test_25(self):
        self.assertEqual(day_25.part_1(day_25.sample_data), 14897079)

        self.assertEqual(day_25.part_1(day_25.challenge_data), 16902792)


if __name__ == "__main__":
    unittest.main()
