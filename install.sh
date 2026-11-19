#!/usr/bin/env bash
set -eu
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-pyqt6
python3 -m pip install -r requirements.txt
chmod +x run.sh
printf 'VELTRIX OS installed. Start with ./run.sh\n'
