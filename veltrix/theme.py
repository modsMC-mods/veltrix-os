THEMES = {
    "midnight": {"bg": "#0b1020", "surface": "#11182a", "card": "#172039", "text": "#edf3ff", "accent": "#4d7cfe"},
    "aurora": {"bg": "#081a20", "surface": "#0d2b32", "card": "#12414a", "text": "#eafffb", "accent": "#22c7a8"},
    "light": {"bg": "#e9eef8", "surface": "#ffffff", "card": "#dce5f5", "text": "#172039", "accent": "#315eea"},
}

def stylesheet(name):
    t = THEMES.get(name, THEMES["midnight"])
    return f"""
    QWidget {{ background: {t['bg']}; color: {t['text']}; font-family: sans-serif; }}
    QFrame#taskbar {{ background: {t['surface']}; }}
    QPushButton {{ background: {t['card']}; color: {t['text']}; border: 0; border-radius: 8px; padding: 9px 13px; }}
    QPushButton:hover {{ background: {t['accent']}; color: white; }}
    QLineEdit, QTextEdit, QPlainTextEdit, QTreeWidget {{ background: {t['surface']}; color: {t['text']}; border: 1px solid {t['card']}; border-radius: 7px; padding: 7px; }}
    QProgressBar {{ background: {t['card']}; border: 0; border-radius: 7px; height: 22px; text-align: center; }}
    QProgressBar::chunk {{ background: {t['accent']}; border-radius: 7px; }}
    QMenu {{ background: {t['surface']}; color: {t['text']}; }}
    """
