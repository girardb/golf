import pytest
import challenge3

class TestChallenge1(object):
    def test_challenge_3_1(self):
        grid = [[2,4,1], [3,1,2], [1,1,1], [3,3,2]]
        assert challenge3.reorder(grid) == [[1,1,1], [1,2,3], [1,2,4], [2,3,3]]

    def test_challenge_3_2(self):
        grid = [[3,2,1], [2,2,1]]
        assert challenge3.reorder(grid) == [[1,2,2], [1,2,3]]
