import subprocess
import sys

def test_lab02_prints_hello():
    output = subprocess.check_output([sys.executable, "labs/lab02/exercise.py"])
    assert b"Hello, Lab 02" in output
