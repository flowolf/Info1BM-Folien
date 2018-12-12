from pytest import approx
# https://docs.pytest.org/en/latest/reference.html#pytest-approx

# fails: 0.30000000000000004 != 0.3
def test_3_1():
    assert 0.1 + 0.2 == 0.3
    #assert 0.1 + 0.2 != 0.3

# # too awkward
# def test_3_2():
#     assert abs((0.1 + 0.2) - 0.3) < 1e-6
#
# def test_3_3():
#     assert 0.1 + 0.2 == approx(0.3)
