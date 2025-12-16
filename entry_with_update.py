import os
import sys

# ---------------------------------
# Keep original working directory logic
# ---------------------------------
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
os.chdir(root)

# ---------------------------------
# PRIVATE MODE (UPDATES DISABLED)
# ---------------------------------
print("Running private Fooocus build")
print("Auto-updates are disabled")
print("Code is loaded only from this repository")

# ---------------------------------
# IMPORTANT: Do NOT remove this
# This line actually starts Fooocus
# ---------------------------------
from launch import *
