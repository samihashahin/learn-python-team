"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_grade_letter():
    """IF statement with multiple elif"""

    score = 85
    grade = ''

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'F'

    assert grade == 'B'

def test_nested_if():
    """Nested IF statement"""

    age = 20
    has_ticket = True
    result = ''

    if age >= 18:
        if has_ticket:
            result = 'Allowed in'
        else:
            result = 'Buy a ticket first'
    else:
        result = 'Too young'

    assert result == 'Allowed in'


def test_grade_letter_boundaries():
    """IF statement with elif at the exact grade limits"""

    for score, expected in [(90, 'A'), (80, 'B'), (70, 'C'), (69, 'F')]:
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        else:
            grade = 'F'

        assert grade == expected
    