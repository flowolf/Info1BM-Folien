from pytest import raises
import random

# checking for raised Exception
def test_2():
    random.randrange(0, "foo")
    # with raises(ValueError):
    #     random.randrange(0, "foo")
