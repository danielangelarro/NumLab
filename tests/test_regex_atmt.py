import pytest
from automata import Automata
from regex_atmt import check


def test_simple_match():
    assert check("a", "a")
    assert check("a", "b") == False
    assert check("a", "aa") == False
    assert check("ab", "ab")
    assert check("ab", "aab") == False


def test_star_op():
    assert check("a*", "")
    assert check("a*", "a")
    assert check("a*", "aa")
    assert check("a*b", "aaab")
    assert check("a*b", "aaa") == False


def test_or_op():
    assert check("a|b", "a")
    assert check("a|b", "b")
    assert check("a|b", "c") == False
    assert check("a|b|c", "c")


def test_escape_char():
    assert check(r"\(a", "a") == False
    assert check(r"\(a", "(a")
    assert check(r"a\*", "a*")
    assert check(r"a\*", "a") == False
    assert check(r"a\**", "a***")
    assert check(r"a\**", "a")
    assert check(r"a\\*", "a\\\\")


def test_special_chars():
    assert check(r"a..*b", "afoob")
    assert check(r"a.*b", "ab")
    assert check(r"a.*b", "afoob")
    assert check(r"a\sb", "a b")
    assert check(r"a\nb", "a\nb")
    assert check(r"a\tb", "a\tb")
    assert check(r"a\rb", "a\rb")
    assert check(r"a\fb", "a\fb")
    assert check(r"a\vb", "a\vb")
    assert check(r"a\a*b", "afoob")
    assert check(r"a\a*b", "aFoob") == False
    assert check(r"a\A*b", "aFOOb")
    assert check(r"a\A*b", "aFoob") == False
    assert check(r"a(\A|\a)*b", "aFoob")
    assert check(r"a\db", "a5b")
    assert check(r"a\d*b", "a5x4b") == False
    assert check(r"a\d*.\db", "a5x4b")


def test_combined_op():
    assert check("aa*|b*", "a")
    assert check("aa*|b*", "b")
    assert check("aa*|b*", "")
    assert check("aa*b*", "a")
    assert check("aa*b*", "b") == False
    assert check("aa*b*", "ab")
    assert check("aa*b*", "aab")
    assert check("(a|b)*", "aabbababa")


def test_negation():
    assert check(r"(^a)", "b")
    assert check(r"(^a)", "a") == False
    assert check(r"(^a)(^a)*", "bcdef")
    assert check(r"'(^')*(^\\)'", "'asfew'")
    assert check(r"'(^')*(^\\)'", "'ab\\'") == False
    assert check(r"'(^')*(^\\)'", "'asfew\\'a") == False
    assert check(r"'(^')*(^\\)'", "'asfew' foo 'bar'") == False
