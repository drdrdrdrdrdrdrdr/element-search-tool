from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt
from search import searchele


class SearchWindow:

    def __init__(self):
        # Initialize the GUI interface.
        self.ui = QUiLoader().load('searchelement.ui')
        self.ui.button.clicked.connect(self.handle)
        self.ui.lineEdit.returnPressed.connect(self.handle)
        self.ui.table.horizontalHeader().setStretchLastSection(True)

    def handle(self):
        # After the button is pushed, fill out the table and textbrowser.
        element = self.ui.lineEdit.text()
        tableinfo, moreinfo = searchele(element)
        if tableinfo == 'error':
            self.ui.textBrowser.setPlainText('查找失败，请输入正确的元素名称！')
            self.ui.table.clearContents()
        else:
            for i in range(6):
                item = QTableWidgetItem()
                item.setText(tableinfo[i])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(0, i, item)
            item = QTableWidgetItem()
            if len(tableinfo) > 6:
                item.setText(','.join(tableinfo[6:]))
            else:
                item.setText('N/A')
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.table.setItem(0, 6, item)
            self.ui.textBrowser.setPlainText(f'查找成功!\n该元素的类别为:{moreinfo[0]}\n电子层排布为:{moreinfo[1]}\n'
                                             f'宇宙中丰度:{moreinfo[2]}%\n太阳系中丰度:{moreinfo[3]}%\n海洋中丰度:'
                                             f'{moreinfo[4]}%\n人类中丰度:{moreinfo[5]}%')
