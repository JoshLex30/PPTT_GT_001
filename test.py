import os
import subprocess
import time
import webbrowser
#import requests#
import winreg


repos = [name for name in os.listdir(git_dir)
        if os.path.isdir(os.path.join(git_dir, name)) and
        os.path.exists(os.path.join(git_dir, name, ".git"))]

git_dir = r"C:\Users\Alexi\OneDrive\Escritorio\Nueva carpeta"
if not os.path.exists(git_dir):
    os.makedirs(git_dir)
    print(f"Created directory: "{git_dir})

if repos:
    print("Found the following GitHub repositor: ")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo}")