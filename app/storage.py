"""Модуль сохранения и загрузки заметок."""
import os

def save(filename, notes):
    """Сохранить заметки в текстовый файл."""
    with open(filename, "w", encoding="utf-8") as f:
        for n in notes:
            f.write(n + "\n")

def load(filename):
    """Загрузить заметки из текстового файла."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()
