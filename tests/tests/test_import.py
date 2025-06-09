def test_import():
    import core.test_trigger
    assert hasattr(core.test_trigger, "__file__")
