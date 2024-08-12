from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

text_edit = QTextEdit()
list_notes_lbl = QLabel("Список заміток")
notes_list = QListWidget()
create_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("зберегти замітку")
teg_list_lbl = QLabel("Список тегів")
add_note_btn = QPushButton("Додати замітку")
vidkriputu_vid_zamitku_btn = QPushButton("Відкріпити від замітки")
teg_input_lbl = QLabel()
find_note_btn = QPushButton("Знайти замітку")


main_line = QHBoxLayout()
main_line.addWidget(text_edit)






v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
v1.addWidget(create_note_btn)
v1.addWidget(save_note_btn)
v1.addWidget(delete_note_btn)
v1.addWidget(teg_list_lbl)
v1.addWidget(add_note_btn)
v1.addWidget(vidkriputu_vid_zamitku_btn)
v1.addWidget(find_note_btn)
main_line.addLayout(v1)

window.setLayout(main_line)
window.show()
app.exec()