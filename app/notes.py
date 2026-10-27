"""Модуль работы с заметками."""

notes = []

def add_note(text):
    """Добавить новую заметку в список."""
    notes.append(text)

def list_notes():
    """Вернуть список всех заметок."""
    return notes

def clear_notes():
    """Очистить список заметок."""
    notes.clear()

def search_notes(keyword):
    """Найти заметки, содержащие ключевое слово."""
    return [n for n in notes if keyword.lower() in n.lower()]

def count_notes():
    """Вернуть количество заметок."""
    return len(notes)
