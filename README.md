# ci-cd-lab

Лабораторная работа №2. CI/CD с GitHub Actions.

## Описание

Python-приложение — консольный блокнот с функциями добавления, просмотра, очистки и поиска заметок, а также сохранения/загрузки в текстовый файл.

## Функции

- `add_note(text)` — добавить заметку
- `list_notes()` — получить список заметок
- `clear_notes()` — очистить заметки
- `search_notes(keyword)` — поиск по заметкам
- `count_notes()` — количество заметок
- `get_last_note()` — последняя заметка
- `save(filename, notes)` — сохранить в файл
- `load(filename)` — загрузить из файла

## CI/CD

Workflow `.github/workflows/main.yml` запускается автоматически:

- при push в любую ветку
- при pull request в `main`

Шаги CI:

1. Checkout кода
2. Установка Python 3.11
3. Установка зависимостей (`pip install -r requirements.txt`)
4. Линтинг через Ruff (`ruff check app/`)
5. Запуск тестов через pytest (`pytest tests/ -v`)

Ветка `main` защищена: изменения попадают в неё только через pull request, который сливается автоматически после успешной проверки.

## Документация

Workflow `.github/workflows/docs.yml` при каждом изменении `main` собирает HTML-документацию из docstrings (pydoc) и сохраняет её как артефакт `project-docs`.

## Запуск локально

    pip install -r requirements.txt
    pytest tests/ -v

## Версия

Текущая версия: **1.0.0** (см. файл `VERSION`)

## Автор

Olga Shuva
