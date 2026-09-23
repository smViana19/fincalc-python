import pytest

from fincalc import calcular_juros_compostos


def test_juros_compostos_padrao():
    montante = calcular_juros_compostos(1000.0, 5.0, 2)
    assert round(montante, 2) == 1102.5


def test_juros_compostos_capital_negativo():
    with pytest.raises(ValueError):
        calcular_juros_compostos(-1000.0, 5.0, 2)


def test_juros_compostos_taxa_negativa():
    with pytest.raises(ValueError):
        calcular_juros_compostos(1000.0, -5.0, 2)


def test_juros_compostos_anos_negativos():
    with pytest.raises(ValueError):
        calcular_juros_compostos(1000.0, 5.0, -2)
