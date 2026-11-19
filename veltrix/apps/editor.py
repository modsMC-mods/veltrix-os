from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog

class Editor(QWidget):
    def __init__(self):
        super().__init__(); self.file = None; self.text = QTextEdit(); self.text.setAcceptRichText(False)
        new = QPushButton("Nowy"); open_btn = QPushButton("Otwórz"); save = QPushButton("Zapisz")
        new.clicked.connect(self.new_file); open_btn.clicked.connect(self.open_file); save.clicked.connect(self.save_file)
        bar = QHBoxLayout(); bar.addWidget(new); bar.addWidget(open_btn); bar.addWidget(save); bar.addStretch()
        layout = QVBoxLayout(self); layout.addLayout(bar); layout.addWidget(self.text)

    def new_file(self): self.file = None; self.text.clear()
    def open_file(self):
        name, _ = QFileDialog.getOpenFileName(self, "Otwórz", str(Path.home()))
        if name: self.file = name; self.text.setPlainText(Path(name).read_text(encoding="utf-8", errors="replace"))
    def save_file(self):
        if not self.file: self.file, _ = QFileDialog.getSaveFileName(self, "Zapisz", str(Path.home()))
        if self.file: Path(self.file).write_text(self.text.toPlainText(), encoding="utf-8")
