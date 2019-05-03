import pytest
import challenge2

class TestChallenge2(object):
    def test_challenge_2_1(self, capsys):
        challenge2.f('a')
        captured = capsys.readouterr()
        assert captured[0] == """*****\n* a *\n*****\n"""

    def test_challenge_2_2(self, capsys):
        challenge2.f('a b c d')
        captured = capsys.readouterr()
        assert captured[0] =="""*******\n* a b *\n* c d *\n*******\n"""

    def test_challenge_2_3(self, capsys):
        challenge2.f('a b c')
        captured = capsys.readouterr()
        assert captured[0] =="""*****\n* a *\n* b *\n* c *\n*****\n"""

    def test_challenge_2_3(self, capsys):
        challenge2.f('a b')
        captured = capsys.readouterr()
        assert captured[0] =="""*****\n* a *\n* b *\n*****\n"""
