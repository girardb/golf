import pytest
import challenge1

class TestChallenge1(object):
    def test_challenge_1_1(self):
        f = "She believed"
        s = "He lied"
        assert challenge1.c(f,s) == 'S[he] be[lie]ve[d]'
    def test_challenge_1_2(self):
        f = "Dishwasher"
        s = "Her"
        assert challenge1.c(f,s) == 'Dis[h]wash[er]'
    def test_challenge_1_3(self):
        f = "She believed"
        s = "She lied"
        assert challenge1.c(f,s) == '[She] be[lie]ve[d]'

    def test_challenge_1_4(self):
        f = "She believed"
        s = "Shebe lied"
        assert challenge1.c(f,s) == '[She] [belie]ve[d]'
