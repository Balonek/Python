from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from py_form import Ui_MainWindow
from bst import BST
from PySide6.QtGui import QIntValidator, QFont

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.bst = BST(update_description_callback=self.update_description)
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

        validator = QIntValidator(self)
        validator.setBottom(0)
        self.ui.lineEdit.setValidator(validator)

        self.ui.statusbar.setFixedHeight(50)
        font = self.ui.statusbar.font()
        font.setPointSize(20)
        self.ui.statusbar.setFont(font)

        self.ui.InsertButton.clicked.connect(self.insert_node)
        self.ui.SearchButton.clicked.connect(self.search_node)
        self.ui.DeleteButton.clicked.connect(self.delete_node)
        self.ui.DeleteWholeTreeButton.clicked.connect(self.clear_tree)

    def insert_node(self):
        value = self.ui.lineEdit.text()
        self.bst.insert(int(value))
        self.ui.lineEdit.clear()
        self.bst.visualize(self.scene)

    def delete_node(self):
        value = self.ui.lineEdit.text()
        self.bst.remove(int(value))
        self.ui.lineEdit.clear()
        self.bst.visualize(self.scene)

    def search_node(self):
        value = self.ui.lineEdit.text()
        result = self.bst.search(int(value))
        if result:
            self.ui.statusbar.showMessage(f"Znaleziono {value}", 3000)
            self.ui.lineEdit.clear()
        else:
            self.ui.statusbar.showMessage(f"Nie znaleziono {value}", 3000)
            self.ui.lineEdit.clear()

    def clear_tree(self):
        self.bst.clear()
        self.scene.clear()
        self.ui.statusbar.showMessage("Drzewo zostało usunięte", 3000)

    def update_description(self):
        text = ""
        if self.bst.size() == 0:
            text = "Drzewo jest puste."
        else:
            text += f"Liczba elementów: {self.bst.size()}<br>"
            text += f"Głębokość drzewa: {self.bst.depth()}<br>"
            text += f"Minimum: {self.bst.minimum()}<br>"
            text += f"Maksimum: {self.bst.maximum()}<br>"
            text += "Inorder: " + " ".join(map(str, self.bst.inorder())) + "<br>"
            text += "Preorder: " + " ".join(map(str, self.bst.preorder())) + "<br>"
            text += "Postorder: " + " ".join(map(str, self.bst.postorder())) + "<br>"
        self.ui.label_4.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
