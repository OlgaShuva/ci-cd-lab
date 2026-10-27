from notes import add_note, list_notes
from storage import save

def main():
    add_note("Первая заметка")
    add_note("Вторая заметка")
    print("Заметки:", list_notes())
    save("notes.txt", list_notes())
    print("Сохранено в notes.txt")

if __name__ == "__main__":
    main()
