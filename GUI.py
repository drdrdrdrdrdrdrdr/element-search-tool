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
        if len(info) > 6:
            self.ui.table.setItem(0, 6, QTableWidgetItem(','.join(info[6:])))
        else:
            self.ui.table.setItem(0, 6, QTableWidgetItem('N/A'))
