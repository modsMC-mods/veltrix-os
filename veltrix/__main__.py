import sys
from datetime import datetime
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QMdiArea, QMdiSubWindow, QMenu
from .config import load_config, save_config
from .theme import stylesheet, THEMES
from .apps.terminal import Terminal
from .apps.files import FileManager
from .apps.editor import Editor
from .apps.system import SystemMonitor

class Veltrix(QMainWindow):
    def __init__(self):
        super().__init__(); self.config = load_config(); self.setWindowTitle("VELTRIX OS"); self.resize(1200, 760); self.setStyleSheet(stylesheet(self.config["theme"]))
        self.mdi = QMdiArea(); self.setCentralWidget(self.mdi); self.make_taskbar(); self.make_icons(); self.timer = QTimer(self); self.timer.timeout.connect(self.clock); self.timer.start(1000); self.clock()
        if self.config.get("fullscreen"): self.showFullScreen()

    def make_icons(self):
        panel = QWidget(self.mdi); panel.setStyleSheet("background: transparent;"); box = QVBoxLayout(panel); box.setContentsMargins(25, 25, 0, 0)
        for text, callback in (("TERMINAL", self.terminal), ("PLIKI", self.files), ("EDYTOR", self.editor), ("SYSTEM", self.system)):
            button = QPushButton(text); button.setFixedSize(100, 58); button.clicked.connect(callback); box.addWidget(button)
        box.addStretch(); panel.setGeometry(0, 0, 130, 500); panel.show()

    def make_taskbar(self):
        bar = QFrame(); bar.setObjectName("taskbar"); bar.setFixedHeight(56); row = QHBoxLayout(bar)
        start = QPushButton("V"); start.clicked.connect(self.menu); row.addWidget(start)
        for text, callback in (("Terminal", self.terminal), ("Pliki", self.files), ("Edytor", self.editor)):
            button = QPushButton(text); button.clicked.connect(callback); row.addWidget(button)
        row.addStretch(); self.clock_label = QLabel(); row.addWidget(self.clock_label); self.statusBar().addPermanentWidget(bar, 1)

    def menu(self):
        menu = QMenu(self)
        for text, callback in (("Terminal", self.terminal), ("Menedżer plików", self.files), ("Edytor", self.editor), ("Monitor systemu", self.system), ("Motyw", self.theme), ("Wyjdź", self.close)):
            action = menu.addAction(text); action.triggered.connect(callback)
        menu.exec(self.mapToGlobal(self.rect().bottomLeft()))

    def clock(self): self.clock_label.setText(datetime.now().strftime("%d.%m.%Y  %H:%M:%S"))
    def open_app(self, title, widget):
        sub = QMdiSubWindow(); sub.setWidget(widget); sub.setWindowTitle(title); sub.resize(760, 500); self.mdi.addSubWindow(sub); sub.show(); sub.raise_()
    def terminal(self): self.open_app("Terminal", Terminal(self.config["safe_terminal"]))
    def files(self): self.open_app("Menedżer plików", FileManager())
    def editor(self): self.open_app("Edytor tekstu", Editor())
    def system(self): self.open_app("Monitor systemu", SystemMonitor())
    def theme(self):
        menu = QMenu(self)
        for name in THEMES:
            action = menu.addAction(name.title()); action.triggered.connect(lambda _=False, n=name: self.set_theme(n))
        menu.exec(self.mapToGlobal(self.rect().center()))
    def set_theme(self, name): self.config["theme"] = name; save_config(self.config); self.setStyleSheet(stylesheet(name))
    def closeEvent(self, event): save_config(self.config); event.accept()

def main():
    app = QApplication(sys.argv); window = Veltrix(); window.show(); sys.exit(app.exec())

if __name__ == "__main__": main()
