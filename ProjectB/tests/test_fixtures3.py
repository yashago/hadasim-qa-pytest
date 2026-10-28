 
def test_one(user):
    assert user.get("name") == "Alice"
 
def test_two(user):
    assert user.get("active") is True

def test_thrtee(user):
    assert user.keys() == {"id", "name", "role", "active"}
