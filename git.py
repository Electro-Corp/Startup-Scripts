# Am I up to date? 
import os
import subprocess
from pathlib import Path

def git(f):
    try:
        result = subprocess.check_output(["git", "-C", f, "status"], stderr=subprocess.STDOUT)
        result.strip(b'\n')
        waa = result.split(b" ")
        if b"behind" in waa:
          print(f"[INFO] {f} can be updated.")
    except subprocess.CalledProcessError as e:
        # whatever 
        pass

for f in os.listdir(Path.home()):
    path = os.path.join(Path.home(), f)
    if os.path.isdir(path):
        git(path)
