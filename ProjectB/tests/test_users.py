
def test_user_name(user):
    assert user["name"] == "Alice"


def test_user_is_active(user):
    assert user["active"] is True


def test_user_role(user):
    assert user["role"] == "admin"
