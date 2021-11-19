from parser import Parser

import pytest
from grammar import Grammar


@pytest.fixture
def parser():
    gm = Grammar.open("./tests/grammars/math_expr.gm")
    return Parser(gm)


# Test first set calculation
def test_calculate_first_set(parser: Parser):
    parser.calculate_first()

    correct_first = {
        "Expr": ["'('", "i"],
        "Expr_X": ["'+'", "EPS"],
        "Term": ["'('", "i"],
        "Term_Y": ["'*'", "EPS"],
        "Factor": ["'('", "i"]
    }

    for expr, first_list in correct_first.items():
        for item in first_list:
            assert item in parser._first[expr]

# Test follow set calculation
def test_calculate_follow_set(parser: Parser):
    parser.calculate_follow()

    correct_follow = {
        "Expr": ["')'", "$"],
        "Expr_X": ["')'", "$"],
        "Term": ["'+'", "')'", "$"],
        "Term_Y": ["'+'", "')'", "$"],
        "Factor": ["'+'", "')'", "'*'", "$"],
    }

    for expr, follow_list in correct_follow.items():
        assert len(follow_list) == len(parser._follow[expr])
        for item in follow_list:
            assert item in parser._follow[expr]
    