#!/bin/bash
cd /home/nexuss0781/Desktop/Nex/Calisthenics-Prototype
source venv/bin/activate
python3 run.py &
sleep 2
xdg-open http://127.0.0.1:5000
