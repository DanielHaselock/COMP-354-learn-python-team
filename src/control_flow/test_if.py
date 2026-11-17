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



def test_multiple_elif_conditions():
    """Demonstrate multiple elif conditions"""

    grade = 85
    result = ''

    if grade >= 90:
        result = 'Excellent'
    elif grade >= 80:
        result = 'Very Good'
    elif grade >= 70:
        result = 'Good'
    elif grade >= 60:
        result = 'Pass'
    else:
        result = 'Fail'

    assert result == 'Very Good'


def test_nested_if_conditions():
    """Demonstrate nested if conditions"""

    age = 20
    is_student = True
    discount = False

    if age >= 18:
        if is_student:
            discount = True

    assert discount is True

    # Additional check: student adults consistently receive a discount
    discount2 = False
    if age >= 18:
        if is_student:
            discount2 = True
    assert discount2 is True
