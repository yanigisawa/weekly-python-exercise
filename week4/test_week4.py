# Passwords are a necessary evil in today's world; every app and Web site asks you to create a login, and then to create a password so that you can use that login. (Let's ignore our ability to use Facebook and Twitter to log into numerous sites.)

# Each site also tries to ensure that your password will be a good one. But what constitutes a good password? That is a judgment call, and every site has its own idea of what is important. Some require a certain number of capital letters, some lowercase letters, some a mixture, some need punctuation, and some need digits. How many of each one differs from site to site.

# This week, we're going to create a function that can be used to create numerous password checkers. That is, our function will take four parameters: min_uppercase, min_lowercase, min_punctuation, and min_digits. These four parameters represent the minimum number of uppercase, lowercase, punctuation, and digits needed for a password to be considered good.

# The output from this create_password_checker is a function, one which takes a potential password (string) as its input, and returns a two-element tuple: The first is a boolean value, indicating whether the password passed the validation test. The second element of the tuple is a dictionary whose keys are "uppercase", "lowercase", "punctuation", and "digits" and whose values represent by how much we've exceeded the minimum. If we haven't achieved the minimum, then the value will be a negative number.

# For example, let's say that we want our passwords to contain at least 2 uppercase letters, at least 3 lowercase letters, at least 1 punctuation mark, and at least 4 digits.  We can create a new password-checking function as follows:
#     pc1 = create_password_checker(2, 3, 1, 4)

# Now let's check ourselves some passwords:
#     print(pc1('Ab!1'))
#     print(pc1('ABcde!1234'))

# Here are the results:
#     (False, {'uppercase': -1, 'lowercase': -2, 'punctuation': 0, 'digits': -3})
#     (True, {'uppercase': 0, 'lowercase': 0, 'punctuation': 0, 'digits': 0})

# We can see that the first password doesn't pass inspection, but that the second does. In the first case, we can see that 1 uppercase letter, 2 lowercase letters, and 3 digits were missing from what would otherwise been a good password.

# I'll be back on Monday with my solution.

from solution import create_password_checker
from string import ascii_uppercase as uppercase, ascii_lowercase as lowercase, punctuation, digits
import pytest

def test_no_min_no_pw():
    pc = create_password_checker(0,0,0,0)
    result, details = pc('')

    assert result
    for key, value in details.items():
        assert value == 0

def test_no_min_some_pw():
    pc = create_password_checker(0,0,0,0)
    result, details = pc('ABCDefgh!@#$1234')

    assert result
    for key, value in details.items():
        assert value == 4

def test_simple_good():
    pc = create_password_checker(1,2,3,4)
    result, details = pc('Abc!@#1234')
    assert result
    for key, value in details.items():
        assert value == 0

def test_simple_bad():
    pc = create_password_checker(1,2,3,4)
    result, details = pc('b!#234')
    assert result == False
    for key, value in details.items():
        assert value == -1

@pytest.mark.parametrize('onlyset', [
    'uppercase',
    'lowercase',
    'punctuation',
    'digits'])
def test_only_set_one(onlyset):
    for source in ['uppercase', 'lowercase', 'punctuation', 'digits']:
        if onlyset == source:
            pw = globals()[source][:4]

    pc = create_password_checker(4,4,4,4)
    result, details = pc(pw)

    assert result == False
    for key, value in details.items():
        if key == onlyset:
            assert value == 0
        else:
            assert value == -4

@pytest.mark.parametrize('donotset', [
    'uppercase',
    'lowercase',
    'punctuation',
    'digits'])
def test_only_ignore_one(donotset):
    pw = ''
    for source in ['uppercase', 'lowercase', 'punctuation', 'digits']:
        if donotset == source:
            continue
        pw += globals()[source][:4]

    pc = create_password_checker(4,4,4,4)
    result, details = pc(pw)

    assert result == False
    for key, value in details.items():
        if key == donotset:
            assert value == -4
        else:
            assert value == 0