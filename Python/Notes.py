import json
import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = datetime.datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'timestamp': str(self.timestamp)
        }

class Notes:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for note_data in data:
                    note = Note(note_data['id'], note_data['title'], note_data['body'])
                    note.timestamp = datetime.datetime.fromisoformat(note_data['timestamp'])
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        with open(self.filename, 'w') as f:
            data = [note.to_dict() for note in self.notes]
            json.dump(data, f)

    def add_note(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, id, title, body):
        note = self.get_note_by_id(id)
        if note:
            note.title = title
            note.body = body
            note.timestamp = datetime.datetime.now()
            self.save_notes()

    def delete_note(self, id):
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)
            self.save_notes()

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def get_notes_by_date(self, date):
        notes = []
        for note in self.notes:
            if note.timestamp.date() == date.date():
                notes.append(note)
        return notes

    def print_notes(self, notes):
        for note in notes:
            print(f'{note.id}. {note.title} ({note.timestamp})\n{note.body}\n')

    def print_all_notes(self):
        self.print_notes(self.notes)

    def run(self):
        while True:
            print('1. Show all notes')
            print('2. Add a note')
            print('3. Edit a note')
            print('4. Delete a note')
            print('5. Show notes by date')
            print('0. Exit')

            choice = input('Enter your choice: ')
            if choice == '1':
                self.print_all_notes()
            elif choice == '2':
                title = input('Enter the title of the note: ')
                body = input('Enter the body of the note: ')
                self.add_note(title, body)
            elif choice == '3':
                id = int(input('Enter the ID of the note to edit: '))
                title = input('Enter the new title of the note: ')
                body = input('Enter the new body of the note: ')
                self.edit_note(id, title, body)
            elif choice == '4':
                id = int(input('Enter the ID of the note to delete: '))
                self.delete_note(id)
            elif choice == '5':
                date_str = input('Enter the date (YYYY-MM-DD) to show notes: ')
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                notes = self.get_notes_by_date(date)
                self.print_notes(notes)
            elif choice == '0':
                break

if __name__ == '__main__':
    notes = Notes('notes.json')
    notes.run()