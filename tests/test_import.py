"""Smoke tests for ai_thai."""

def test_import():
    import ai_thai
    assert hasattr(ai_thai, "translate")
