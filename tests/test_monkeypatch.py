import os
 
def get_mode():
    qaModeEnvParam = os.getenv("QA_MODE", "production")
    print(f"qaModeEnvParam: {qaModeEnvParam}")
    return qaModeEnvParam
 
def test_mode_can_be_overridden(monkeypatch):
    monkeypatch.setenv("QA_MODE", "test")
    print(f"QA_MODE: {os.getenv('QA_MODE')}")
    monkeypatch.setattr()
    assert get_mode() == "test"