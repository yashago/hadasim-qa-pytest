import pytest
import shutil

@pytest.fixture
def temporary_directory(tmp_path):
    # Setup phase
    print("\nSetup: Creating temporary files")
    (tmp_path / "data.txt").write_text("Test data", encoding="utf-8")
    print(f"\nCreated tmp_path: {tmp_path}")
    yield tmp_path  # Test executes here

    # Teardown phase
    print("\nTeardown: Deleting temporary directory", tmp_path)
    # shutil.rmtree(tmp_path)

def test_temporary_directory(temporary_directory):
    # Use the temporary directory in the test
    temp_file = temporary_directory / "data.txt"
    assert temp_file.exists()
    assert temp_file.read_text(encoding="utf-8") == "Test data"