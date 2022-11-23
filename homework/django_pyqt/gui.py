import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget, QPushButton
from guiapp.models import Note


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input = QLineEdit()
        self.upd_input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        self.upd_input.textChanged.connect(self.label.setText)

        self.button = QPushButton("Delete user")
        self.button.clicked.connect(self.remove())

        self.button = QPushButton("Update user")
        self.button.clicked.connect(self.update())

        self.button = QPushButton("Create a new user")
        self.button.clicked.connect(self.create_())

        self.button = QPushButton("Get user")
        self.button.clicked.connect(self.read())

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.upd_input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

    def remove(self):
        request = Note.objects.filter(user=self.input).delete()
        return request

    def update(self):
        request = Note.objects.get(user=self.input).delete()
        upd_request = request.user.get(user=self.upd_input)
        return upd_request

    def create_(self):
        request = Note.objects.create(user=self.input)
        return request

    def read(self):
        request = Note.objects.get(user=self.input)
        return request


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()