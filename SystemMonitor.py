from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QSlider, QPushButton
from tinydb import TinyDB

from HistoryWindow import HistoryWindow
from sysInfoReader import *



class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.minPeriod = 500
        self.maxPeriod = 2000
        self.startPeriod = 1000
        self.writeFlag = False
        self.pathToDB = "./monitorDB.json"
        self.db = TinyDB(self.pathToDB)
        self.writeTime = 0

        self.setWindowTitle("PySystemMonitor")
        self.cpuLabel = QLabel()
        self.ramLabel = QLabel()
        self.romLabel = QLabel()
        self.header = QLabel()
        self.header.setText("System load:")


        self.updateTimer = QTimer()

        self.updateTimer.timeout.connect(self.updateSysInfo)
        self.updateTimer.start(self.startPeriod)

        self.updateSlider = QSlider(Qt.Orientation.Horizontal)
        self.updateSlider.setRange(self.minPeriod, self.maxPeriod)
        self.updateSlider.setSingleStep(5)
        self.updateSlider.setSliderPosition(self.startPeriod)
        self.updateSlider.valueChanged.connect(self.updateTimerPeriod)

        self.updateSL = QLabel()
        self.updateSL.setText(f"Update rate: {self.startPeriod} ms")

        self.writeButton = QPushButton()
        self.writeButton.setText("Start record")
        self.writeButton.clicked.connect(self.invertWriteFlag)
        self.clearHistory = QPushButton()
        self.clearHistory.setText("Clear history DB")
        self.clearHistory.clicked.connect(self.clearDB)
        self.seeHistory = QPushButton()
        self.seeHistory.setText("See history")
        self.seeHistory.clicked.connect(self.seeHistoryW)

        layout = QVBoxLayout()
        layout.addWidget(self.header)
        layout.addWidget(self.cpuLabel)
        layout.addWidget(self.ramLabel)
        layout.addWidget(self.romLabel)
        layout.addWidget(self.updateSL)
        layout.addWidget(self.updateSlider)
        layout.addWidget(self.writeButton)
        layout.addWidget(self.seeHistory)
        layout.addWidget(self.clearHistory)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    def updateSysInfo(self):
        cpu = readCPULoad()
        ram = readRAMLoad()
        rom = readROMLoad()

        self.cpuLabel.setText(f"CPU: {cpu} %")
        self.ramLabel.setText(f"RAM (available/used/total): {ram} MB")
        self.romLabel.setText(f"ROM (free/used/total): {rom} MB")

        if self.writeFlag:
            self.writeTime += self.updateTimer.interval()
            self.writeButton.setText(f"Recording...({self.writeTime/1000} s)")
            self.db.insert({"cpu": cpu, "ram": ram, "rom": rom})
        else:
            self.writeButton.setText("Start record")


    def updateTimerPeriod(self, value):
        self.updateSL.setText(f"Update rate: {value} ms")
        self.updateTimer.setInterval(value)

    def invertWriteFlag(self):
        self.writeFlag = not(self.writeFlag)

    def clearDB(self):
        self.db.truncate()

    def seeHistoryW(self):
        self.historyW = HistoryWindow(data=self.db.all())
        self.historyW.show()
