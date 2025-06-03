import subprocess
import sys
import os
import signal
import time

# 1. Install backend dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"])

# 2. Install frontend dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "frontend/requirements.txt"])

# 3. Launch backend
backend_proc = subprocess.Popen(
    [sys.executable, "app.py"],
    cwd="backend"
)

# 4. Small delay to let backend start before frontend
time.sleep(2)

# 5. Launch frontend via Voilà
frontend_proc = subprocess.Popen(
    ["voila", "run.ipynb"],
    cwd="frontend"
)

# 6. Wait until either process exits
try:
    while True:
        if backend_proc.poll() is not None or frontend_proc.poll() is not None:
            break
        time.sleep(1)
finally:
    # 7. Terminate both if one exits or on Ctrl+C
    for proc in (backend_proc, frontend_proc):
        if proc and proc.poll() is None:
            proc.send_signal(signal.SIGTERM)
