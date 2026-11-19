# VELTRIX OS

Działające środowisko desktopowe dla Linuksa napisane w Pythonie i PyQt6.

## Uruchomienie

```bash
chmod +x install.sh run.sh
./install.sh
./run.sh
```

Alternatywnie: `python3 -m pip install -r requirements.txt && python3 -m veltrix`.

## Funkcje

Pulpit, menu V, terminal z bezpiecznym trybem, menedżer plików, edytor, monitor CPU/RAM/dysku, trzy motywy oraz konfiguracja w `~/.config/veltrix-os/config.json`.

Terminal domyślnie pozwala tylko na polecenia odczytujące informacje o systemie. Nowe aplikacje dodaje się jako klasy QWidget w `veltrix/apps/`.
