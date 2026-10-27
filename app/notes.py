notes = []

def add_note(text):
    notes.append(text)

def list_notes():
    return notes

def clear_notes():
    notes.clear()

def search_notes(keyword):
    return [n for n in notes if keyword.lower() in n.lower()]
