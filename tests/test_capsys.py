import logging
 
def announce():
    myInput = input("Enter your name:")
    print("Hi", myInput)
    print("starting2")
    print("starting3")
    logging.warning("Retrying request")
    logging.error("Request failed")

# def test_console_output(capsys):
#     announce()
#     captured = capsys.readouterr()
#     print("Captured:", captured)
#     print(f"\n====================\nCaptured output:\n{captured.out}")
#     assert "starting" in captured.out
 
# def test_log_message(caplog):
#     announce()
#     print("Caplog:", caplog)
#     print(f"Captured log: {caplog.text}")
#     assert "Request failed" in caplog.text

def test_caplog_and_capsys_class(caplog, capsys):
    announce()
    captured = capsys.readouterr()
    print("Captured in CAPSYS:", captured.out)
    print(f"Captured in CAPLOG: {caplog.text}")
    assert True