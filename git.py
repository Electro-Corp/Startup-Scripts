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
          print(f"{f} can be updated.")
         #print(f"{f} is up to date.")
    except subprocess.CalledProcessError as e:
        pass
        #print(f"{f} is not a valid Git repository or an error occurred: {e.output.decode()}")

for f in os.listdir(Path.home()):
    path = os.path.join(Path.home(), f)
    if os.path.isdir(path):
        git(path)
