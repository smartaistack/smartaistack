import sys
import os
from core.test_trigger import test_trigger  # noqa: F401

# Legg til path slik at 'core' kan importeres
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


def test_import():
    assert True
