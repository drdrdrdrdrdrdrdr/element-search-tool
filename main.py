from GUI import SearchWindow
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon


app = QApplication([])
app.setWindowIcon(QIcon('logo.png'))
searchwindow = SearchWindow()
searchwindow.ui.show()
app.exec_()
