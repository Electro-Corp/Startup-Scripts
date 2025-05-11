# Tool to quickly show me the biggest directory on startup
import os
import subprocess
from pathlib import Path

def get_folder_size(path):
    result = subprocess.run(['du', '-sb', path], stdout=subprocess.PIPE)
    size_in_bytes = int(result.stdout.split()[0])
    return size_in_bytes

def find_largest_folder(directory):
    largest_folder = None
    largest_size = 0
    
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            folder_size = get_folder_size(folder_path)
            
            if folder_size > largest_size:
                largest_size = folder_size
                largest_folder = folder_path

    return largest_folder, largest_size


directory = Path.home()
largest_folder, largest_size = find_largest_folder(directory)

if largest_folder:
  if largest_size / (1024 * 1024) > 1024:
    print(f"[INFO] Largest Folder is {largest_folder} at {largest_size / (1024 * 1024 * 1024):.2f} GB")
  else:
    print(f"[INFO] Largest folder is {largest_folder} at {largest_size / (1024 * 1024):.2f} MB")

