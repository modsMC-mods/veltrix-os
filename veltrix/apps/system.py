from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
import psutil

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__(); layout = QVBoxLayout(self); self.labels = {}; self.bars = {}
        for key in ("CPU", "RAM", "DYSK"):
            self.labels[key] = QLabel(); self.bars[key] = QProgressBar(); layout.addWidget(self.labels[key]); layout.addWidget(self.bars[key])
        layout.addStretch(); self.timer = QTimer(self); self.timer.timeout.connect(self.refresh); self.timer.start(1000); self.refresh()

    def refresh(self):
        values = {"CPU": psutil.cpu_percent(), "RAM": psutil.virtual_memory().percent, "DYSK": psutil.disk_usage('/').percent}
        for key, value in values.items(): self.labels[key].setText(f"{key}: {value:.1f}%"); self.bars[key].setValue(int(value))
