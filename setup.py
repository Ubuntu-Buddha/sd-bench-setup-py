# Bench fixture: inert text.
import os
os.system("echo bench-fixture-setup > bench-marker.txt")
from setuptools import setup
setup(name="sd-bench-setup-py", version="0.0.1")
