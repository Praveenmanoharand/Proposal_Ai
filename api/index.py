import sys
import os

# Ensure the root path is in sys.path so app.py can be loaded
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from app import app
