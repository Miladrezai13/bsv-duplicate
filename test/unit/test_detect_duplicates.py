import pytest
from src.util.parser import Article
from src.util.detector import detect_duplicates

# TC1: Unique Articles
def test_detect_duplicates_unique_articles():
    data = """
    @article{a1, doi={10.1000/abc123}}
    @article{a2, doi={10.1000/xyz456}}
    @article{a3, doi={10.1000/uvw789}}
    """
    result = detect_duplicates(data)
    assert result == [], "Expected no duplicates for unique articles."

# TC2: Duplicates (Key and DOI)
def test_detect_duplicates_key_and_doi():
    data = """
    @article{a1, doi={10.1000/abc123}}
    @article{a1, doi={10.1000/abc123}}
    """
    result = detect_duplicates(data)
    assert len(result) == 1, "Expected one duplicate for identical key and DOI."

# TC3: Duplicates (Key Only)
def test_detect_duplicates_key_only():
    data = """
    @article{a1}
    @article{a1}
    """
    result = detect_duplicates(data)
    assert len(result) == 1, "Expected one duplicate for identical key only."

# TC4: Multiple Duplicates
def test_detect_duplicates_multiple_duplicates():
    data = """
    @article{a1, doi={10.1000/abc123}}
    @article{a1, doi={10.1000/abc123}}
    @article{a2}
    @article{a2}
    """
    result = detect_duplicates(data)
    assert len(result) == 2, "Expected two duplicates for two sets of duplicates."

# TC5: Less Than Two Articles
def test_detect_duplicates_insufficient_articles():
    data = """
    @article{a1, doi={10.1000/abc123}}
    """
    with pytest.raises(ValueError, match="The input data does not contain enough articles"):
        detect_duplicates(data)

# TC6: Empty Input
def test_detect_duplicates_empty_input():
    data = ""
    with pytest.raises(ValueError, match="The input data does not contain enough articles"):
        detect_duplicates(data)

# TC7: file with articles missing keys
def test_detect_duplicates_missing_keys():
    data = """
    @article{, doi={10.1000/abc123}}
    @article{a1, doi={10.1000/xyz456}}
    """
    result = detect_duplicates(data)
    assert result == [], "Expected no duplicates for articles with missing keys."

