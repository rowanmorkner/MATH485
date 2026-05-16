# conftest.py — shared pytest configuration and fixtures
import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_df():
    """A small DataFrame available to all tests for convenience."""
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "age": [25, 30, 35, 28, 22],
        "score": [88.5, 92.0, 75.3, 95.1, 81.7],
        "city": ["NYC", "LA", "NYC", "Chicago", "LA"],
    })
