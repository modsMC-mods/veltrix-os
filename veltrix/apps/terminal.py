from PyQt6.QtCore import QProcess
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPlainTextEdit

SAFE = {"pwd", "ls", "whoami", "date", "uname", "id", "uptime", "df", "free", "clear", "help"}

class Terminal(QWidget):
    def __init__(self, safe=True):
        super().__init__(); self.safe = safe; self.process = None
        self.output = QPlainTextEdit(readOnly=True); self.input = QLineEdit()
        self.input.setPlaceholderText("Polecenie — help pokazuje listę")
        self.input.returnPressed.connect(self.execute)
        layout = QVBoxLayout(self); layout.addWidget(QLabel("VELTRIX Terminal")); layout.addWidget(self.output); layout.addWidget(self.input)
        self.output.appendPlainText("Terminal gotowy. Bezpieczny tryb: " + ("ON" if safe else "OFF"))

    def execute(self):
        command = self.input.text().strip(); self.input.clear()
        if not command: return
        if command == "clear": self.output.clear(); return
        if command == "help": self.output.appendPlainText("Dozwolone: " + ", ".join(sorted(SAFE))); return
        if self.safe and command.split()[0] not in SAFE:
            self.output.appendPlainText("Zablokowano w bezpiecznym trybie."); return
        self.process = QProcess(self); self.process.setProgram("/bin/sh"); self.process.setArguments(["-c", command])
        self.process.readyReadStandardOutput.connect(self.read); self.process.readyReadStandardError.connect(self.read); self.process.start()

    def read(self):
        data = bytes(self.process.readAllStandardOutput()).decode(errors="replace")
        data += bytes(self.process.readAllStandardError()).decode(errors="replace")
        self.output.appendPlainText(data.rstrip())
