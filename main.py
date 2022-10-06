from GUI import SearchWindow
from PySide2.QtWidgets import QApplication


app = QApplication([])
searchwindow = SearchWindow()
searchwindow.ui.show()
app.exec_()
