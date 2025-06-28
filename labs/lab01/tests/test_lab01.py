import subprocess, sys

def test_lab01_prints_hello():
    out = subprocess.check_output([sys.executable, "labs/lab01/exercise.py"])
    assert b"Hello, Lab 01" in out
