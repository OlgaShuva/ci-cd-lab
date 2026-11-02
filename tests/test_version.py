from pathlib import Path


def test_version_is_1_0_0():
    assert Path("VERSION").read_text().strip() == "1.0.0"
