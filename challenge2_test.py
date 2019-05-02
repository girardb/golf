import pytest
import challenge2

class TestChallenge2(object):
    def test_challenge_2_1(self, capsys):
        list_of_words = ['a']
        challenge2.print_in_a_frame(list_of_words, challenge2.permut(list_of_words[1:] ,[[list_of_words[0]]], 0))
        captured = capsys.readouterr()
        assert captured[0] == """*****\n* a *\n*****\n"""

    def test_challenge_2_2(self, capsys):
        list_of_words = ['a', 'b', 'c', 'd']
        challenge2.print_in_a_frame(list_of_words, challenge2.permut(list_of_words[1:] ,[[list_of_words[0]]], 0))
        captured = capsys.readouterr()
        assert captured[0] =="""*******\n* a b *\n* c d *\n*******\n"""


    def test_challenge_2_3(self, capsys):
        list_of_words = ['a', 'b', 'c']
        challenge2.print_in_a_frame(list_of_words, challenge2.permut(list_of_words[1:] ,[[list_of_words[0]]], 0))
        captured = capsys.readouterr()
        assert captured[0] =="""*****\n* a *\n* b *\n* c *\n*****\n"""

    def test_challenge_2_3(self, capsys):
        list_of_words = ['a', 'b']
        challenge2.print_in_a_frame(list_of_words, challenge2.permut(list_of_words[1:] ,[[list_of_words[0]]], 0))
        captured = capsys.readouterr()
        assert captured[0] =="""*****\n* a *\n* b *\n*****\n"""
