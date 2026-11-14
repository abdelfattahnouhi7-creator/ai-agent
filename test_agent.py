import pytest
from agent import calculate_invoice

def test_normal():
    assert calculate_invoice(["100 DH", "200,50", 50], 10) == 315.45

def test_liste_khawya():
    with pytest.raises(ValueError):
        calculate_invoice([], 10)

def test_taman_salib():
    with pytest.raises(ValueError):
        calculate_invoice(["100 DH", -20], 10)

def test_remise_kbira():
    with pytest.raises(ValueError):
        calculate_invoice([100], 150)

def test_mad_ou_dirham():
    assert calculate_invoice(["100 MAD", "100 درهم"], 0) == 200.0

def test_none_marfoud():
    with pytest.raises(ValueError):
        calculate_invoice([100, None], 10)
