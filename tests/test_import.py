import sys
import os

# Legg til repo-roten i sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.test_trigger import test_trigger  # noqa: F401

def test_import():
    assert True
