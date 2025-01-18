from PyQt6.QtWidgets import QApplication, QWidget
from SystemMonitor import SystemMonitor
import sys



app = QApplication(sys.argv)

window = SystemMonitor()
window.show()


app.exec()
