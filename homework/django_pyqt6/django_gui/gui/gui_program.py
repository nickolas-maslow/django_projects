from PyQt6.QtWidgets import QMainWindow, QLineEdit, QApplication, QGridLayout, QPushButton, QWidget
import sys
from .models import User


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('DjangoGui')

        self.layout = QGridLayout()

        self.request = QLineEdit(self)
        self.btn_create = QPushButton('Create user', self)
        self.btn_update = QPushButton('Update user', self)
        self.btn_delete = QPushButton('Delete user', self)
        self.btn_get = QPushButton('Get user', self)

        self.layout.addWidget(self.request, 1, 1)
        self.layout.addWidget(self.btn_create, 2, 1)
        self.layout.addWidget(self.btn_update, 3, 1)
        self.layout.addWidget(self.btn_delete, 4, 1)
        self.layout.addWidget(self.btn_get, 5, 1)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def create_user(self):
        return User.objects.create(name=self.request)

    def delete_user(self):
        return User.objects.get(name=self.request).delete()

    def update_user(self):
        return User.objects.update({'name': self.request})

    def get_user(self):
        return User.objects.all(name=self.request)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())