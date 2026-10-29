import pytest

@pytest.mark.parametrize(
        "username, expected", [
            pytest.param("myUsername", True, id="Should be OK"),
            pytest.param("usr", False, id="Too short"),
            pytest.param("MyusernameIsVeryLong", False, id="Very long"),
            ]
)
def test_usernameLength(username, expected):
    assert isPasswordValid(username) == expected

#This is what I actually test
def isPasswordValid(name):
    lenUsrname = len(name)
    return lenUsrname > 3 and lenUsrname < 12
    