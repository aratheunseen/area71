from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QWidget,\
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("About", self)
        help_menu_item.addAction(add_student_action)

        about_action = QAction("Add Student", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)

        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * from students")

        self.table.setRowCount(0)
        for row_index, row_data in enumerate(result):
            self.table.insertRow(row_index)
            for column_index, data in enumerate(row_data):
                self.table.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        connection.close()


app = QApplication(sys.argv)

student_management_system = MainWindow()
student_management_system.show()
student_management_system.load_data()
sys.exit(app.exec())