import json
import shutil
import tempfile
import urllib.request
from pathlib import Path

import pytest

DESERTS_URL = "https://raw.githubusercontent.com/sharmadhiraj/free-json-datasets/refs/heads/master/docs/geography-environment/largest_deserts_in_the_world.json"


def download_desert_file():
    temp_dir = Path(tempfile.mkdtemp(prefix="deserts_"))
    deserts_path = temp_dir / "largest_deserts_in_the_world.json"
    urllib.request.urlretrieve(DESERTS_URL, deserts_path)
    return deserts_path


def delete_deserts_file(deserts_file):
    shutil.rmtree(deserts_file.parent, ignore_errors=True)


@pytest.fixture(scope="module")
def deserts_json():
    deserts_file = download_desert_file()
    json_content = json.loads(deserts_file.read_text(encoding="utf-8"))
    yield json_content
    delete_deserts_file(deserts_file)

def test_title(deserts_json):
    assert deserts_json.get("title") == "World’s Major Deserts by Area (2025)"

def test_deserts_json_content(deserts_json):
    print(f"Deserts JSON content: {len(deserts_json.get('data'))}")
    assert len(deserts_json.get("data")) == 38