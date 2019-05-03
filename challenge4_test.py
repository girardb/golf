import pytest
import challenge4

class TestChallenge4(object):
    def test_challenge_4_1(self):
        equation='(3 * 4) * 2 + 1'
        assert challenge4.s(equation) == '3 4 * 2 * 1 +'

    def test_challenge_4_2(self):
        equation='(5 - 6) * 2 / (1 + 3)'
        assert challenge4.s(equation) == '5 6 - 2 * 1 3 + /'

    def test_challenge_4_3(self):
        equation='(4 - 1) / (2 - 3)'
        assert challenge4.s(equation) == '4 1 - 2 3 - /'

    def test_challenge_4_4(self):
        equation='((5 - 3) * ((4 / 2 - 1) * 2))'
        assert challenge4.s(equation) == '5 3 - 4 2 / 1 - 2 * *'

    def test_challenge_4_5(self):
        equation='(4 ^ 2) * 3'
        assert challenge4.s(equation) == '4 2 ^ 3 *'

    def test_challenge_4_6(self):
        equation='4 ^ (3 - 1)'
        assert challenge4.s(equation) == '4 3 1 - ^'

    def test_challenge_4_7(self):
        equation='((4+7)*12+2)/4'
        assert challenge4.s(equation) == '4 7 + 12 * 2 + 4 /'

    def test_challenge_4_8(self):
        equation='(((((((((1+2)))))))))'
        assert challenge4.s(equation) == '1 2 +'

    def test_challenge_4_9(self):
        equation='(((12)+(21)))'
        assert challenge4.s(equation) == '12 21 +'
