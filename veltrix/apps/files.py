from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTreeWidget, QTreeWidgetItem, QPushButton

class FileManager(QWidget):
    def __init__(self):
        super().__init__(); self.current = Path.home(); self.path = QLineEdit(); self.tree = QTreeWidget(); self.tree.setHeaderLabels(["Nazwa", "Typ", "Rozmiar"]); self.tree.itemDoubleClicked.connect(self.open_item)
        go = QPushButton("Idź"); go.clicked.connect(lambda: self.load(self.path.text()))
        home = QPushButton("Dom"); home.clicked.connect(lambda: self.load(Path.home()))
        bar = QHBoxLayout(); bar.addWidget(self.path); bar.addWidget(go); bar.addWidget(home)
        layout = QVBoxLayout(self); layout.addLayout(bar); layout.addWidget(self.tree); self.load(self.current)

    def load(self, value):
        folder = Path(value).expanduser()
        if not folder.is_dir(): return
        self.current = folder; self.path.setText(str(folder)); self.tree.clear()
        try: entries = sorted(folder.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        except OSError: entries = []
        for entry in entries:
            try: size = "folder" if entry.is_dir() else f"{entry.stat().st_size // 1024} KB"
            except OSError: size = "?"
            self.tree.addTopLevelItem(QTreeWidgetItem([entry.name, "Folder" if entry.is_dir() else "Plik", size]))

    def open_item(self, item, _column):
        target = self.current / item.text(0)
        if target.is_dir(): self.load(target)
