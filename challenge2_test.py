import pytest
import challenge2

class TestChallenge3(object):
    def test_challenge_3_1(capsys):
        challenge2.print_in_a_frame(['a'], permut([] ,[[list_of_words[0]]], 0))
        captured = capsys.readouterr()
        assert captured.out ==
        """
         *
        *

        """
