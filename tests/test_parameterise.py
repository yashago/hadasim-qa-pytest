import pytest

@pytest.mark.parametrize(
        "myDay", [
            pytest.param("Sun", id="Sunday"),
            pytest.param("Mon", id="Monday"),
            pytest.param("Tue", id="Monday"),
            ]
)
def test_myDays(myDay):
    print(f"My day: {myDay}")
    assert True

# def add(a, b):
#     return a+b

# @pytest.mark.parametrize(
#     "a, b, expected, name",
#     [
#         pytest.param(2, 3, 5, "myName", id="positive-numbers"),
#         pytest.param(0, 5, 5, "myName", id="zero-plus-positive"),
#         pytest.param(-2, 3, 1, "myName", id="negative-plus-positive"),
#         pytest.param(-2, 4, 2, "myName", id="negative-plus-positive"),
#     ],
# )
# def test_add(a, b, expected, name):
#     print(f"Running test:", name)
#     assert add(a, b) == expected