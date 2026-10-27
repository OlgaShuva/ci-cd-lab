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
- `save(filename, notes)` — сохранить в файл
- `load(filename)` — загрузить из файла

## CI/CD

GitHub Actions workflow `.github/workflows/main.yml` автоматически запускается при:

- push в `main`, `development`, `release`
- pull request в `main`

Шаги CI:

1. Checkout кода
2. Установка Python 3.11
3. Установка зависимостей (`pip install -r requirements.txt`)
4. Линтинг через Ruff (`ruff check app/`)
5. Запуск тестов через pytest (`pytest tests/ -v`)

## Запуск локально

Установка зависимостей и запуск тестов:

    pip install -r requirements.txt
    pytest tests/ -v

(команды выше можно скопировать в терминал)

## Версия

Текущая версия: **1.0.0** (см. файл `VERSION`)

## Автор

Olga Shuva
