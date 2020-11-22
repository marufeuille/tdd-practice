import pytest

@pytest.fixture(scope="session")
def init():
    from pathlib import Path
    import sys
    sys.path.append(str(Path(__file__).parent.parent / "src"))