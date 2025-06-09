import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core import test_trigger  # noqa: F401

def test_import():
    assert True
