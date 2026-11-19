#!/usr/bin/env bash
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python3 -m pip install -r "$ROOT/requirements.txt"
exec python3 -m veltrix
