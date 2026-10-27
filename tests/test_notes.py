import sys
sys.path.insert(0, 'app')

from notes import add_note, list_notes, clear_notes, search_notes

def test_add_note():
    clear_notes()
    add_note("test")
    assert "test" in list_notes()

def test_clear_notes():
    add_note("a")
    clear_notes()
    assert list_notes() == []

def test_search_notes():
    clear_notes()
    add_note("Python CI")
    add_note("GitHub Actions")
    assert "Python CI" in search_notes("python")
    assert "GitHub Actions" not in search_notes("python")
