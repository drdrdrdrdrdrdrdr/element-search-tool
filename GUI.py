from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QTableWidgetItem
from search import searchele


class SearchWindow:

    def __init__(self):
        self.ui = QUiLoader().load('searchelement.ui')
        self.ui.button.clicked.connect(self.handle)
        self.ui.table.horizontalHeader().setStretchLastSection(True)

    def handle(self):
        element = self.ui.lineEdit.text()
        info = searchele(element)
        for i in range(6):
            self.ui.table.setItem(0, i, QTableWidgetItem(info[i]))
        self.ui.table.setItem(0, 6, QTableWidgetItem(info[6]+','+info[7]+','+info[8]))


app = QApplication([])
searchwindow = SearchWindow()
searchwindow.ui.show()
app.exec_()
