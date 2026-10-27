import sys, os
sys.path.insert(0, 'app')

from storage import save, load

def test_save_and_load(tmp_path):
    filename = str(tmp_path / "test.txt")
    save(filename, ["line1", "line2"])
    assert os.path.exists(filename)
    result = load(filename)
    assert result == ["line1", "line2"]

def test_load_nonexistent(tmp_path):
    filename = str(tmp_path / "nope.txt")
    assert load(filename) == []
