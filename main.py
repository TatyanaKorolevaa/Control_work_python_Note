import os
import json


class Notes:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                self.notes = json.load(file)

    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)
            
    def list_notes(self):
        if not self.notes:
            print("У вас нет заметок.")
        else:
            print("Список ваших заметок:")
            for idx, note in enumerate(self.notes):
                print(f"{idx + 1}. {note['title']}")        

    def create_note(self, title, content):
        note = {"title": title, "content": content}
        self.notes.append(note)
        self.save_notes()
        print(f"Заметка '{title}' успешно создана.")


    def edit_note(self, index, new_title, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index]["title"] = new_title
            self.notes[index]["content"] = new_content
            self.save_notes()
            print(f"Заметка успешно отредактирована.")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            deleted_note = self.notes.pop(index)
            self.save_notes()
            print(f"Заметка '{deleted_note['title']}' успешно удалена.")

if __name__ == "__main__":
    app = Notes()
    app.load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Список заметок")
        print("2. Создать заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            app.list_notes()
        elif choice == "2":
            title = input("Введите заголовок: ")
            content = input("Введите текст: ")
            app.create_note(title, content)
        elif choice == "3":
            index = int(input("Введите номер заметки для редактирования: ")) - 1
            if 0 <= index < len(app.notes):
                new_title = input("Введите новый заголовок: ")
                new_content = input("Введите новый текст: ")
                app.edit_note(index, new_title, new_content)
            else:
                print("Такой заметки не существует. Укажите номер заметки.")
        elif choice == "4":
            index = int(input("Введите номер заметки для удаления: ")) - 1
            if 0 <= index < len(app.notes):
                app.delete_note(index)
            else:
                print("Такой заметки не существует. Укажите номер заметки.")
        elif choice == "5":
            break
        else:
            print("Для выбора действия укажите номер от 1 до 5")