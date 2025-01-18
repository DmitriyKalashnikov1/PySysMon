from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView


class HistoryWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.rowCount = len(data)

        self.setWindowTitle("History")
        self.historyTable = QTableWidget()
        self.historyTable.setColumnCount(3)
        self.historyTable.setHorizontalHeaderLabels(["CPU (%)", "RAM (available/used/total) (Mb)", "ROM (free/used/total) (Mb)"])

        header = self.historyTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        for rowP in range(self.rowCount):
            cpuItem = QTableWidgetItem()
            cpuItem.setText(data[rowP]["cpu"])
            ramItem = QTableWidgetItem()
            ramItem.setText(data[rowP]["ram"])
            romItem = QTableWidgetItem()
            romItem.setText(data[rowP]["rom"])
            self.historyTable.insertRow(rowP)
            self.historyTable.setItem(rowP, 0, cpuItem)
            self.historyTable.setItem(rowP, 1, ramItem)
            self.historyTable.setItem(rowP, 2, romItem)

        layout = QVBoxLayout()
        layout.addWidget(self.historyTable)

        container = QWidget()
        container.setLayout(layout)
        container.setMinimumSize(550, 400)

        self.setCentralWidget(container)
