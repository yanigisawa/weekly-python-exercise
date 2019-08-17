

# @once_per_minute
# def hello(name):
#     return "Hello, {}".format(name)

# for i in range(30):
#     print(i)
#     try:
#         time.sleep(3)
#         print(hello("attempt {}".format(i)))
#     except TooSoonError as e:
#         print("Too soon: {}".format(e))


import pytest
import time
from solution import once_per_minute, TooSoonError

@once_per_minute
def hello(name):
    return f"Hello, {name}"

def test_run_once(capsys):
    assert hello('world') == 'Hello, world'

def test_run_twice_in_a_row(capsys):
    with capsys.disabled():
        print("Waiting to run")
    time.sleep(60)
    assert hello('world') == 'Hello, world'

    with pytest.raises(TooSoonError) as e:
        hello('world 2')

def test_run_waiting_59_sec(capsys):
    with capsys.disabled():
        print("Waiting to run")
    time.sleep(60)

    assert hello('world') == 'Hello, world'
    time.sleep(59)

    with pytest.raises(TooSoonError) as e:
        hello('world 2')
        assert 'Wait another 1.' in str(e)